import platform
import sys
import numpy as np

OS = platform.system()
print(f"Detected OS: {OS}")

# ---------------- WINDOWS / LINUX (AMD/NVIDIA) ----------------
if OS in ["Windows", "Linux"]:
    try:
        import os
        import pyopencl as cl
        os.environ['PYOPENCL_COMPILER_OUTPUT'] = '1'
        print("Using PyOpenCL for GPU stress test")

        # Select first GPU device
        platform_ = cl.get_platforms()[0]
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
        kernel = cl.Kernel(prg, "matmul")  # reuse kernel to avoid warning

        print("Starting GPU stress test. Press Ctrl+C to stop.")
        while True:
            kernel(queue, (N, N), None, a_g, b_g, res_g, np.int32(N))
            queue.finish()

    except Exception as e:
        print(f"Failed to run PyOpenCL GPU stress test: {e}")
        sys.exit(1)

# ---------------- MACOS (Apple GPU) ----------------
elif OS == "Darwin":
    try:
        import tensorflow as tf
        print("Using TensorFlow (Metal) for GPU stress test")

        gpus = tf.config.list_physical_devices('GPU')
        if not gpus:
            print("No GPU found on Mac.")
            sys.exit(1)
        print(f"Detected GPUs: {[gpu.name for gpu in gpus]}")

        N = 8192  # Adjust based on GPU memory
        x = tf.random.normal((N, N))

        print("Starting GPU stress test. Press Ctrl+C to stop.")
        while True:
            x = tf.matmul(x, x)  # matrix multiply to stress GPU

    except Exception as e:
        print(f"Failed to run TensorFlow GPU stress test: {e}")
        sys.exit(1)

else:
    print(f"OS {OS} is not supported for GPU stress test.")
    sys.exit(1)
