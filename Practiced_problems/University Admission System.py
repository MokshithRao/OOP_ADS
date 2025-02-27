class Applicant:
    def __init__(self, applicantID, name, score):
        self.applicantID = applicantID
        self.name = name
        self.score = score

    def getApplicantInfo(self):
        return f"{self.applicantID}, {self.name}, {self.score}"
    

class Application:
    def __init__(self, applicationID, applicantID, programApplied):
        self.applicationID = applicationID
        self.applicantID = applicantID
        self.programApplied = programApplied

    def getApplicationDetails(self):
        return f"{self.applicationID}, {self.applicantID}, {self.programApplied}"
    


class AdmissionOffice:
    def __init__(self, applicants, applications):
        self.applicants = applicants
        self.applications = applications

    def submitApplication(self, application):
        self.applications.append(application)

    def reviewApplication(self, applicantID):
        for app in self.applications:
            if applicantID == app.applicantID:
                return "Accepted"
        return "Not Accepted"







def main():
    # Create applicants and applications
    applicant1 = Applicant(1, "Sara", 92.5)
    applicant2 = Applicant(2, "Tom", 85.0)
    application1 = Application(101, 1, "Computer Science")
    application2 = Application(102, 2, "Mathematics")

    office = AdmissionOffice([], [])
    office.applicants.extend([applicant1, applicant2])
    office.applications.extend([application1, application2])

    # Submit an application
    office.submitApplication(application1)
    print("Application submitted for", applicant1.name)


    # Review applications
    review1 = office.reviewApplication(1)
    review_invalid = office.reviewApplication(999)
    print("Review outcome for applicant 1:", review1)
    print("Review outcome for non-existent applicant:", review_invalid)

if __name__ == '__main__':
    main()