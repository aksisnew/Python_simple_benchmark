import math
import hashlib
import random
import json
import re
import time
import multiprocessing
import platform
import psutil

def get_system_info():
    system_info = {
        "Platform": platform.platform(),
        "CPU Cores": multiprocessing.cpu_count(),
        "Total RAM": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
    }
    return system_info

def t1(n):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for _ in range(n):
        if 4 * q + r - t < m * t:
            q, r, t, k, m, x = 10 * q, 10 * (r - m * t), t, k, (10 * (3 * q + r)) // t - 10 * m, x
        else:
            q, r, t, k, m, x = q * k, (2 * q + r) * x, t * x, k + 1, (q * (7 * k + 2) + r * x) // (t * x), x + 2
    return True, n

def t2(n):
    p =[]
    for num in range(2, n):
        i_p = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                i_p = False
                break
        if i_p:
            p.append(num)
    return True, n

def t3(n):
    r = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(r[i-1][j-1] + r[i-1][j])
        row.append(1)
        r.append(row)
    return True, n

def t4(n):
    c =[]
    for num in range(4, n):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                c.append(num)
                break
    return True, n

def t5(n):
    d = b"b" * 1024
    for _ in range(n):
        hashlib.sha1(d).hexdigest()
        hashlib.sha512(d).hexdigest()
    return True, n

def t6(n):
    l = [random.random() for _ in range(n)]
    l.sort()
    return True, n

def t7(n):
    c = 0
    for _ in range(n):
        for y in range(2026, 22026):
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                c += 1
    return True, n * (22026 - 2026)

def t8(n):
    v = 1.0
    for i in range(1, n):
        v = (v * 1.000001) / 1.0000005 + math.sin(i % 10)
    return True, n

def t9(n):
    for _ in range(n):
        d = {"a": random.randint(1, 10000), "b": random.randint(1, 10000)}
        s = json.dumps(d)
        json.loads(s)
    return True, n

class N:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def t10(n):
    r = None
    def i(rt, v):
        if not rt: return N(v)
        if v < rt.v: rt.l = i(rt.l, v)
        else: rt.r = i(rt.r, v)
        return rt
    def s(rt, v):
        if not rt or rt.v == v: return rt
        if rt.v < v: return s(rt.r, v)
        return s(rt.l, v)
    l =[]
    for _ in range(n):
        if random.random() > 0.5:
            v = hex(random.randint(100000, 999999999))
        else:
            v = str(random.randint(100000, 999999999))
        l.append(v)
        r = i(r, v)
    for v in l[:1000]:
        s(r, v)
    j = ",".join(l)
    re.findall(r"0x[a-f0-9]+", j)
    re.findall(r"\b\d+\b", j)
    return True, n

def t11(n):
    v = 1000000000.0
    for i in range(1, n):
        v /= (1.0 + (i % 10) * 0.001)
    return True, n

def t12(n):
    m_size = int(math.sqrt(n))
    matrix_a = [[random.random() for _ in range(m_size)] for _ in range(m_size)]
    matrix_b = [[random.random() for _ in range(m_size)] for _ in range(m_size)]
    result_matrix = [[0 for _ in range(m_size)] for _ in range(m_size)]
    for i in range(m_size):
        for j in range(m_size):
            for k in range(m_size):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return True, m_size**3

def t13(n):
    inside_circle = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside_circle += 1
    return True, n

def t14(n):
    def fib(num):
        if num <= 1:
            return num
        else:
            return fib(num-1) + fib(num-2)
    for i in range(n):
        fib(15)
    return True, n

def t15(n):
    long_string = "abcdefghijklmnopqrstuvwxyz" * 100
    pattern = r"[aeiou]"
    for _ in range(n):
        re.findall(pattern, long_string)
    return True, n

def rs(m):
    ts_config =[
        ("1_pi", t1, 12000, 6000, "iterations"),
        ("2_primes", t2, 80000, 40000, "numbers checked"),
        ("3_pascal", t3, 4800, 2400, "rows generated"),
        ("4_composite", t4, 120000, 60000, "numbers checked"),
        ("5_crypto", t5, 800000, 400000, "hash operations"),
        ("6_sort", t6, 6000000, 3000000, "elements sorted"),
        ("7_leap", t7, 800, 400, "year checks"),
        ("8_float", t8, 16000000, 8000000, "iterations"),
        ("9_json", t9, 200000, 100000, "json operations"),
        ("10_bst_regex", t10, 32000, 16000, "bst/regex operations"),
        ("11_division", t11, 24000000, 12000000, "iterations"),
        ("12_matrix_mult", t12, 2000, 1000, "matrix multiplications"),
        ("13_monte_carlo", t13, 4000000, 2000000, "simulations"),
        ("14_fibonacci", t14, 10000, 5000, "fibonacci calculations"),
        ("15_string_regex", t15, 40000, 20000, "regex operations")
    ]
    r = {}
    if m:
        c_cpu = multiprocessing.cpu_count()
        p = multiprocessing.Pool(c_cpu)
        for n_test, f, single_param, multi_param, metric_desc in ts_config:
            st = time.time()
            results = p.map(f, [multi_param]*c_cpu)
            et = time.time()
            time_taken = et - st
            total_count = sum(res[1] for res in results if isinstance(res, tuple))
            r[n_test] = {"time": time_taken, "count": total_count, "metric": metric_desc}
        p.close()
        p.join()
    else:
        for n_test, f, single_param, multi_param, metric_desc in ts_config:
            st = time.time()
            passed, count = f(single_param)
            et = time.time()
            time_taken = et - st
            r[n_test] = {"time": time_taken, "count": count, "metric": metric_desc}
    return r

def main():
    st_t = time.time()

    print("SYSTEM INFORMATION:")
    info = get_system_info()
    for k, v in info.items():
        print(f"{k}: {v}")
    print("\n")

    time.sleep(2) 

    r_s = rs(False)
    r_m = rs(True)
    ed_t = time.time()

    print("SINGLE CORE BENCHMARK:")
    for k, metrics in r_s.items():
        time_taken = metrics["time"]
        count = metrics["count"]
        metric_desc = metrics["metric"]
        print(f"Test {k}: {time_taken:.4f}s, Operations: {count} {metric_desc}")

    print("\nMULTI CORE BENCHMARK:")
    for k, metrics in r_m.items():
        time_taken = metrics["time"]
        count = metrics["count"]
        metric_desc = metrics["metric"]
        print(f"Test {k}: {time_taken:.4f}s, Operations: {count} {metric_desc}")

    print(f"\nTotal Time Elapsed: {ed_t - st_t:.4f}s")

if __name__ == '__main__':
    main()
