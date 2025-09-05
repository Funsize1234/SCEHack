import pyopencl as cl
import numpy as np

# Setup OpenCL
platform = cl.get_platforms()[0]          # pick first platform
device = platform.get_devices()[0]        # pick first device (your AMD GPU)
ctx = cl.Context([device])
queue = cl.CommandQueue(ctx)

# Create large arrays
N = 8192
a_np = np.random.rand(N, N).astype(np.float32)
b_np = np.random.rand(N, N).astype(np.float32)
res_np = np.empty_like(a_np)

mf = cl.mem_flags
a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
b_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)
res_g = cl.Buffer(ctx, mf.WRITE_ONLY, res_np.nbytes)

# OpenCL kernel for matrix multiplication
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

# Stress loop
while True:
    prg.matmul(queue, (N, N), None, a_g, b_g, res_g, np.int32(N))
