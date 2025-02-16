from src.entities.Resume import Resume, PersonalInformation, Date, Address, Contact, Link, ProfessionalDescription, Experience, Job, Organization, Education, Degree, Language, Project, Award


class RandomResumeGenerator:
    def generate_resume(self):
        personal = self.__generate_personal()
        professional = self.__generate_professional()
        experience = self.__generate_experience()
        education = self.__generate_education()
        skills = self.__generate_skills()
        languages = self.__generate_languages()
        projects = self.__generate_projects()
        awards = self.__generate_awards()
        publications = self.__generate_publications()
        patents = self.__generate_patents()
        scores = self.__generate_scores()
        memberships = self.__generate_memberships()
        causes = self.__generate_causes()
        references = self.__generate_references()

        return Resume(
            personal=personal,
            professional=professional,
            experience=experience,
            education=education,
            skills=skills,
            languages=languages,
            projects=projects,
            awards=awards,
            publications=publications,
            patents=patents,
            scores=scores,
            memberships=memberships,
            causes=causes,
            references=references
        )

    def __generate_personal(self):
        return PersonalInformation(
            name="Carl Johnson",
            age=Date(start="1971-08-17", end="", duration="54 years"),
            address=Address(
                number="789",
                street="Ganton St",
                city="Los Santos",
                state="San Andreas",
                postal_code="90210",
                country="USA"
            ),
            civil_status="Single",
            contact=Contact(
                emails=["cj@gta.com"],
                phones=["+1800-00-8765432109"],
                websites=["https://cjsgarage.com"]
            ),
            links=[
                Link(type="Twitter", url="https://twitter.com/CJ_GTA"),
                Link(type="Instagram", url="https://instagram.com/CJ_LS")
            ]
        )

    def __generate_professional(self):
        return ProfessionalDescription(
            title="Entrepreneur and Leader",
            summary="Former gang leader turned successful businessman and community leader in Los Santos."
        )

    def __generate_experience(self):
        return Experience(
            jobs=[
                Job(
                    title="Owner and CEO",
                    description="Founder and CEO of CJ's Garage, providing top-notch car modifications and street racing services.",
                    contract_type="Full-time",
                    organization=Organization(
                        name="CJ's Garage",
                        industry="Automotive",
                        address=Address(
                            number="",
                            street="",
                            city="Los Santos",
                            state="SA",
                            postal_code="",
                            country=""
                        ),
                        contact=Contact(emails=[], phones=[], websites=[])
                    ),
                    date=Date(start="1992-01", end="", duration="33 years")
                ),
                Job(
                    title="Gang Leader",
                    description="Led the Grove Street Families in reclaiming control of Los Santos and restoring the gang's dominance.",
                    contract_type="Full-time",
                    organization=Organization(
                        name="Grove Street Families",
                        industry="",
                        address=Address(
                            number="",
                            street="",
                            city="Los Santos",
                            state="SA",
                            postal_code="",
                            country=""
                        ),
                        contact=Contact(emails=[], phones=[], websites=[])
                    ),
                    date=Date(
                        start="1992-01",
                        end="2004-12",
                        duration="12 years"
                    )
                )
            ],
            volunteering=[]
        )

    def __generate_education(self):
        return Education(
            degrees=[
                Degree(
                    title="Street Smarts and Leadership",
                    description="Learned from experience, navigating the streets of Los Santos and managing various enterprises.",
                    field_of_study="Streetwise Leadership",
                    organization=Organization(
                        name="Los Santos University",
                        industry="Education",
                        address=Address(
                            number="",
                            street="",
                            city="Los Santos",
                            state="SA",
                            postal_code="",
                            country=""
                        ),
                        contact=Contact(
                            emails=[],
                            phones=[],
                            websites=["www.los-santos-university.edu"]
                        )
                    ),
                    date=Date(
                        start="1988-01-01",
                        end="1992-01-01",
                        duration="4 years"
                    )
                )
            ],
            certifications=[]
        )

    def __generate_skills(self):
        return [
            "Street Racing",
            "Negotiation",
            "Business Management",
            "Guns & Tactics",
            "Leadership",
            "Car Modification"
        ]

    def __generate_languages(self):
        return [
            Language(language="English", proficiency="Native"),
            Language(language="Spanish", proficiency="Basic")
        ]

    def __generate_projects(self):
        return Project(
            title="Grove Street Restoration",
            description="Led efforts to reclaim and revitalize Grove Street, bringing peace and prosperity back to the neighborhood.",
            role="Leader",
            organization=Organization(
                name="Grove Street Families",
                industry="",
                address=Address(
                    number="",
                    street="",
                    city="Los Santos",
                    state="SA",
                    postal_code="",
                    country=""
                ),
                contact=Contact(emails=[], phones=[], websites=[])
            ),
            date=Date(start="1992-01", end="2004-12", duration="12 years")
        )

    def __generate_awards(self):
        return [
            Award(
                title="Grove Street Legend",
                description="Recognized as a leader who brought peace and prosperity to Grove Street and the surrounding areas.",
                organization=Organization(
                    name="Los Santos Population",
                    industry="",
                    address=Address(
                        number="",
                        street="",
                        city="Los Santos",
                        state="SA",
                        postal_code="",
                        country=""
                    ),
                    contact=Contact(emails=[], phones=[], websites=[])
                ),
                date=Date(
                    start="2004-12",
                    end="",
                    duration=""
                )
            )
        ]

    def __generate_publications(self):
        return []

    def __generate_patents(self):
        return []

    def __generate_scores(self):
        return []

    def __generate_memberships(self):
        return []

    def __generate_causes(self):
        return [
            "Grove Street Uprising",
            "Business in the Hood"
        ]

    def __generate_references(self):
        return []
