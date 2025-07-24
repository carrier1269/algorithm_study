import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final int MOD = 1_000_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long n = Long.parseLong(br.readLine());

        long result = fibo(n);
        System.out.println(result);
    }

    private static long fibo(long n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        long[][] matrix = {{1, 1}, {1, 0}};
        long[][] result = matrixPow(matrix, n - 1);

        return result[0][0] % MOD;
    }

    private static long[][] matrixMultiply(long[][] a, long[][] b) {
        int rowA = a.length;
        int colA = a[0].length;
        int colB = b[0].length;
        long[][] result = new long[rowA][colB];

        for (int i = 0; i < rowA; i++) {
            for (int j = 0; j < colB; j++) {
                for (int k = 0; k < colA; k++) {
                    result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % MOD;
                }
            }
        }

        return result;
    }

    private static long[][] matrixPow(long[][] matrix, long exponent) {
        if (exponent == 1) {
            return matrix;
        }

        if (exponent % 2 == 0) {
            long[][] halfPow = matrixPow(matrix, exponent / 2);
            return matrixMultiply(halfPow, halfPow);
        } else {
            return matrixMultiply(matrix, matrixPow(matrix, exponent - 1));
        }
    }
}
