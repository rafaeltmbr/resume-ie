from dataclasses import dataclass


@dataclass
class Date:
  start: str
  end: str
  duration: str

@dataclass
class Contact:
  emails: list[str]
  phones: list[str]
  websites: list[str]

@dataclass
class Address:
  number: str
  street: str
  city: str
  state: str
  postal_code: str
  country: str

@dataclass
class Organization:
  name: str
  industry: str
  address: Address
  contact: Contact

@dataclass
class Link:
  type: str
  url: str

@dataclass
class PersonalInformation:
  name: str
  age: Date
  address: Address
  civil_status: str 
  contact: Contact
  links: list[Link]

@dataclass
class ProfessionalDescription:
  title: str
  summary: str

@dataclass
class Language:
  language: str
  proficiency: str

@dataclass
class Job:
  title: str
  description: str
  contract_type: str
  organization: Organization
  date: Date

@dataclass
class Experience:
  jobs: list[Job]
  volunteering: list[Job]

@dataclass
class Degree:
  title: str
  description: str
  field_of_study: str
  organization: Organization
  date: Date

@dataclass
class Certification:
  title: str
  description: str
  organization: Organization
  date: Date

@dataclass
class Education:
  degrees: list[Degree]
  certifications: list[Certification]
 
@dataclass
class Project:
  title: str
  description: str
  role: str
  organization: Organization
  date: Date

@dataclass
class Award:
  title: str
  description: str
  organization: Organization
  date: Date

@dataclass
class Publication:
  title: str
  type: str
  date: Date
  link: Link

@dataclass
class Membership:
  type: str
  organization: Organization
  date: Date

@dataclass
class Reference:
  person: PersonalInformation
  organization: Organization

 
@dataclass
class Resume:
  personal: PersonalInformation
  professional: ProfessionalDescription
  skills: list[str]
  languages: list[Language]
  experience: Experience
  education: Education
  projects: list[Project]
  awards: list[Award]
  publications: list[Publication]
  memberships: list[Membership]
  references: list[Reference]
