import stramlit as st
st.title("Kiểm tra số nguyên tố")
n = st.nummer_imput("Nhap mot so:", min_value=1,step=1)
if st.button("Kiem tra"):
    ist_prim=n>=2

    for i in range(2, int(n**0.5) + 1):
      if n % i== 0:
        ist_prim= False
        break
    if ist_prim:
      st.success("Day la snt")
else:
  st.error("Khong phai snt")
