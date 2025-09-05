import numpy as np
import pyopencl as cl
import multiprocessing as mp
import time
import math

def stress_gpu():
  import platform
  OS = platform.system()
  print(f"Detected OS: {OS}")

  print("Using PyOpenCL for GPU stress test")

  # Select first GPU device
  platforms = cl.get_platforms()
  platform_ = platforms[0]
  if OS not in ["Windows", "Linux"]:
    for platform in platforms:
      if 'Apple' in platform.name:
        platform_ = platform
        break

  device = platform_.get_devices()[0]
  ctx = cl.Context([device])
  queue = cl.CommandQueue(ctx)
  print(f"Using platform: {platform_.name}, device: {device.name}")

  # Allocate matrices
  N = 500  # Adjust based on GPU memory
  a_np = np.random.rand(N, N).astype(np.float32)
  b_np = np.random.rand(N, N).astype(np.float32)
  res_np = np.empty_like(a_np)

  mf = cl.mem_flags
  a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
  b_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)
  res_g = cl.Buffer(ctx, mf.WRITE_ONLY, res_np.nbytes)

  # Kernel
  kernel_code = """
  __kernel void matmul(__global const float* A, __global const float* B, __global float* C, int N) {
      int row = get_global_id(0);
      int col = get_global_id(1);
      float sum = 0.0f;
      for (int k = 0; k < N; k++) {
          sum += A[row * N + k] * B[k * N + col];
      }
      C[row * N + col] = sum;
  }
  """
  prg = cl.Program(ctx, kernel_code).build()
  kernel = cl.Kernel(prg, "matmul") 

  print("Starting GPU stress test")

  while True:
      kernel(queue, (N, N), None, a_g, b_g, res_g, np.int32(N))
      queue.finish()

def stress_memory(size_gb):
    size = size_gb * (1024**3) // 8
    arr = np.ones(size, dtype=np.float64)
    print(f"Memory stress started on {size_gb} GB...")
    while True:
        #Interacts with the memory so OS doesn't free it
        arr[:] = arr * 1.0000001
        _ = arr.sum();


if __name__ == "__main__":
    # Run GPU + Memory stress in parallel
    gpu_proc = mp.Process(target=stress_gpu)
    mem_proc = mp.Process(target=stress_memory, args=(8,))  # 4 GB
    gpu_proc.start()
    mem_proc.start()
    gpu_proc.join()
    mem_proc.join()
