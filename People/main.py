import student as s
import worker as w

def main():
    st = s.Student("Jackie", 11, "Middle School")
    wo = w.Worker("Sarbjit", 44, "Nvidia", 10.00)

    st.what_division()
    print(f"Grade: {st.what_grade()}")

    print(f"Cost to hire sarbjit: {wo.cost_to_hire(8)}")

main()