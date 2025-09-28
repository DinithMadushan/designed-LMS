from employee import BCI_salary_Employee,BCI_com_basedEmployee,BCI_part_time_Employee,BCI_Lecture_Employee,BCI_Admin_Employee,BCI_Marketing_Employee,BCI_Cleaner_Employee
from course import BCIDegree,BCIDiploma,BCICertificate
from student import BCIdegreeStudent,BCIdiplomaStudent,BCIcertificateStudent
from findSalary import BCIAcademicSalary,BCINonAcademicSalary
from findaverage import BCIDegreeAverage,BCIDiplomaAverage,BCICertificateAverage
from campus import BCIContact
from faculty import BCIFaculties

def main():
    while True:
        print("                       --------------------------------")
        print("                 ==== |  BCI Campus Management System  | ====")
        print("                       --------------------------------")

        print("1.Employee Details")
        print("2.Courses Details")
        print("3.Students Details")
        print("4.Faculties")
        print("5.Employee Salary Details")
        print("6.Course's Average Details")
        print("7.Contact")
        print("8.Exit")
        print("-------------------------------------------")

        choice = input("Enter your choice: ")


        if choice == "1":

            print("\n==================================================================================================")
            print("\n==Lecturers's Details==\n")
            l1 = BCI_Lecture_Employee("AE001","Susrara")
            l2 = BCI_Lecture_Employee("AE002","Waruna")

            ls_list =[l1,l2]

            for l in ls_list:
                l.showEmployee()


            print("\n==================================================================================================")
            print("\n==Admins's Details==\n")
            adm1 = BCI_salary_Employee("AE001","Susrara")
            adm2 = BCI_salary_Employee("AE002","Waruna")

            adm_list =[adm1,adm2]

            for adm in adm_list:
                adm.showEmployee()


            print("\n==================================================================================================")
            print("\n==Marketing Employee's Details==\n")
            mar1 = BCI_com_basedEmployee("AE001","Susrara")
            mar2 = BCI_com_basedEmployee("AE002","Waruna")

            mar_list =[mar1,mar2]

            for mar in mar_list:
                mar.showEmployee()


            print("\n==================================================================================================")
            print("\n==Part Time Employee's Details==\n")
            pe1 = BCI_part_time_Employee("NAE022","Amal Perera")
            pe2 = BCI_part_time_Employee("NAE123","Kamal Fernando")

            pe_list =[pe1,pe2]

            for pe in pe_list:
                pe.showEmployee()

            print("\n===================================================================================================================")

        elif choice == "2":

            print("\n==================================================================================================")
            print("\n==Degree Courses Details==\n")
            deg = BCIDegree("Software Engineering","BSSE12032","4","Rs.2,200,000")
            deg.showCourses()

            print("\n==================================================================================================")
            print("\n==Diploma Courses Details==\n")
            dip = BCIDiploma("Music Therapy","MT1200","3","Rs.950,000")
            dip.showCourses()

            print("\n==================================================================================================")
            print("\n==Certificate Courses Details==\n")
            cert = BCICertificate("Graphic Design","GD56023","1","Rs.50,000")
            cert.showCourses()

            print("\n===================================================================================================================")

        elif choice == "3":
            print("\n==================================================================================================")
            print("\n==Degree Students Details==\n")
            degStud = BCIdegreeStudent("BSSE241024","Dinith Madushan","Software Engineering","2024","2002-05-15")
            degStud.showStudents()

            print("\n==================================================================================================")
            print("\n==Diploma Students Details==\n")
            dipStud = BCIdiplomaStudent("MT12012","Charith gamage","Music Theraphy","2025","2004-03-12")
            dipStud.showStudents()


            print("\n==================================================================================================")
            print("\n==Certificate Students Details==\n")
            certStud = BCIcertificateStudent("GD32012","Dulni Kodithuwakku","Graphic Design","2025","2005-01-18")
            certStud.showStudents()

            print("\n===================================================================================================================")

        elif choice == "4":
                print("\n===================================================================================================================")

                print("\n==FACULTIES OF BCI==\n")

                f1 = BCIFaculties("1.School of Computing")
                f2 = BCIFaculties("2.School of Business")
                f3 = BCIFaculties("3.School of Music")
                f4 = BCIFaculties("4.School of Psychology & Counselling")
                f5 = BCIFaculties("5.Academy of English")

                fs = [f1,f2,f3]

                for f in fs:
                    f.showFaculties()
                print("\n===================================================================================================================")


        elif choice == "5":
            print("\n==================================================================================================")
            print("\n==Academic Employee Salary Details==\n")
            acad1 = BCIAcademicSalary("Susrara",2000,6*2*4)
            acad2 = BCIAcademicSalary("Waruna",2500,4*5*4)

            acad_list =[acad1,acad2]

            for acad in acad_list:
                acad.showsalary()

            print("\n==================================================================================================")
            print("\n==NonAcademic Employee Salary Details==\n")
            nacad1 = BCINonAcademicSalary("Amal",25000,2500)
            nacad2 = BCINonAcademicSalary("Kamal Fernando",35000,1500)

            nacad_list =[nacad1,nacad2]

            for nacad in nacad_list:
                nacad.showsalary()

            print("\n===================================================================================================================")


        elif choice == "6":
            print("\n==================================================================================================")
            print("\n==Degree Average Details==\n")
            deg_avg = BCIDegreeAverage([18, 15, 10], [15, 20, 15], [35, 40, 50])
            deg_avg.showAverage()

            print("\n==================================================================================================")
            print("\n==Diploma Average Details==\n")
            dip_avg = BCIDiplomaAverage([15,20,18], [55, 70, 62])
            dip_avg.showAverage()


            print("\n==================================================================================================")
            print("\n==Certificate Average Details==\n")
            cert_avg = BCICertificateAverage([88,70,66,90])
            cert_avg.showAverage()


            print("\n===================================================================================================================")


        elif choice == "7":
            print("\n===================================================================================================================")

            c1 = BCIContact("Benedict XVI Catholic International Institute of Higher Education," \
            "\n                      495, Minuwangoda Road,\n                      Bolawalana, Negombo,\n                      Sri Lanka",
                            "0112326598","info@bci.lk")
            c1.showContact()
            print("\n===================================================================================================================")


        elif choice == "8":
            print("Exiting BCI Campus Management System.......")
            break

        else:
            print("Invalid input, please try again!\n")


if __name__ == "__main__" :
    main()