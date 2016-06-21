import Tkinter
import solver


def solve():
    equation = expression_input.get()
    try:
        answer.configure(
            text="x={}".format(solver.solve(equation)),
            font=('Helvetica', 32), foreground="black")
    except solver.NotLinearEquationError:
        err = "Your expression doesn't look like linear equation"
        answer.configure(text=err, font=('Helvetica', 10), foreground="red")

# create a GUI window.
root = Tkinter.Tk()
root.title("Linear equations solver")

# Input label
equation_label = Tkinter.Label(root, text="Linear equation:")
equation_label.grid(row=0, column=0, padx=5, pady=5)

# Label
expression_input = Tkinter.Entry(root, width=36)
expression_input.grid(row=0, column=1, pady=5)

# Button
trigger = Tkinter.Button(root, text="Solve!", command=solve)
trigger.grid(row=0, column=2, padx=5, pady=5)

# Answer label
answer = Tkinter.Label(root, text="")
answer.grid(row=2, column=1, padx=5, pady=5)

# start the GUI
root.mainloop()
