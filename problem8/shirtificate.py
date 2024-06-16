from fpdf import FPDF
class PDF():
    def __init__(self, name):
        self.pdf_ = FPDF()
        self.pdf_.add_page()
        self.pdf_.set_font("helvetica", "", 30)
        self.pdf_.cell(0, 60, "CS50 Shirtificate", align="C")
        self.pdf_.image("shirtificate.png", 10, 70, 190)
        self.pdf_.set_font_size(24)
        self.pdf_.set_text_color(255, 255, 255)
        self.pdf_.text(x=48, y=140, txt=f"{name} took CS50")

    def save(self, name):
        self.pdf_.output(name)
 
def main():
    name = input("Name: ")
    pdf = PDF(name) 
    pdf.save("shirtificate.pdf")  

if __name__ == "__main__":
    main() 