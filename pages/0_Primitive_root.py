import streamlit as st

st.header("Welcome to PRIMITIVE ROOT!")
st.write("What  is your name")

txt_FNAME = st.text_input("FIRST NAME")
txt_LNAME = st.text_input("LAST NAME")

btn_submit = st.button("submit")

if btn_submit:
  st.success(f"Hello {txt_FNAME} {txt_LNAME}|")

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def modulus(base, exponent, mod):
    result = 1
    for _ in range(exponent):
        result = (result * base) % mod
    return result
    
def primitive_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            n = int(user_input)
            if n > 1:
                return n
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Please enter a valid integer")

def primitive_roots(p):
    primitive_root = []
    for g in range(1,p):
        is_primitive = True
        primitive = set()
        for j in range(1,p):
            res = modulus(g,j,p)
            primitive.add(res)
            if res == 1:
                break
        if len(primitive) == p - 1:
            primitive_root.append(g)
    return primitive_root
    
def print_primitive(p, prim_num):
    if not prime(p):
        print(f"{p} is not a prime number!!")
        return
    
    print_result = []
    for g in range(1, p):
        output = []
        for j in range(1, p):
            res = modulus(g, j, p)
            output.append(f"{g}^{j} mod {p} = {res}")
            if res == 1:
                break
        if g in primitive_roots(p):
            output[-1] += f" ==> {g} is primitive root of {p}|"
        else:
            output[-1] += "|"
        print_result.append("|".join(output))
        
    print("\n".join(print_result))
    primitive_root = primitive_roots(p)
    if primitive_root:
        if prim_num in primitive_root:
            print(f"{prim_num} is primitive root: True {primitive_root}")
        else:
            print(f"{prim_num} is NOT primitive root of {p} - List of Primitive roots: {primitive_root}")
    else:
        print(f"{prim_num} is NOT primitive root of {p} - List of Primitive root: {primitive_root}")

p = primitive_input("")
prim_num = primitive_input("")
print_primitive(p, prim_num)
