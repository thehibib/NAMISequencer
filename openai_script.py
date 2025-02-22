import json
import time
from openai import OpenAI
example =  '{"provider": "Attention Deficit Disorder Association (ADDA)","email": "", "phone number": "(800) 939-1019","video": "","website": "https://add.org/","category": "ADHD","description": "Provides information and resources on ADD for adults living with the disorder, including support groups, workshops and an “Ambassadors” program to provide ADD adults an opportunity to talk with others living with the disorder."}'

# import google.generativeai as genai
table_of_contents = {
    "ABUSE": [
        "Child Abuse",
        "Domestic Violence & Sexual Assault",
        "Elder Abuse",
        "Online Abuse"
    ],
    "ATTENTION DEFICIT/HYPERACTIVITY DISORDER": [
        "Adults",
        "Children & Teens"
    ],
    "ADVOCACY": [
        "Mental Health Policy/Self-Advocacy",
        "Patient Advocate Services"
    ],
    "AFRICAN AMERICAN COMMUNITY": [],
    "AGING POPULATIONS": [
        "General",
        "Alzheimer’s/Dementia"
    ],
    "ANOSOGNOSIA": [
        "General",
        "Education and Support",
        "Preparing for a Crisis"
    ],
    "ANXIETY DISORDERS": [],
    "ASIAN AMERICAN COMMUNITY": [],
    "AUTISM SPECTRUM DISORDER (ASD)": [],
    "BIPOLAR DISORDER (BD)": [],
    "BRAIN INJURY": [],
    "CHILDREN & TEENS": [
        "For Parents",
        "For Children & Teens",
        "Crisis Support - Teens"
    ],
    "COMPLAINTS": [
        "Against a Correctional Facility",
        "Against a Housing Facility",
        "Against an Individual Provider",
        "Against a Treatment Facility or Hospital",
        "Insurance Claims",
        "Medical Parity"
    ],
    "CRISIS/EMERGENCY MENTAL HEALTH SERVICES": [
        "Mental Health Crisis",
        "Preparing for a Crisis",
        "Suicidal Ideation Crisis",
        "Teen Crisis Support",
        "Urgent Medication Needs",
        "Urgent Psychiatric Treatment",
        "Urgent Psychotherapy",
        "Veteran Crisis support",
        "988 Suicide & Crisis Lifeline"
    ],
    "DEPRESSION": [],
    "DIAGNOSIS": [
        "General",
        "Online Screening Tools"
    ],
    "DISABILITY BENEFITS (Including SSI & SSDI)": [],
    "DISABILITY RIGHTS": [
        "Education",
        "Employment/Accommodations",
        "Housing Discrimination/Complaints",
        "Incarcerated Persons – Mistreatment While Incarcerated"
    ],
    "DISSOCIATIVE DISORDERS": [],
    "EATING DISORDERS": [],
    "EMOTIONAL SUPPORT": [
        "General",
        "Animals (Emotional Support & Service Dogs)",
        "HealthCare & Frontline Workers",
        "Online & Teleconference Support",
        "Resilience-Building"
    ],
    "EMPLOYMENT": [
        "Accommodations & Discrimination Issues",
        "Finding a Job",
        "Workplace Mental Health"
    ],
    "END-OF-LIFE TRANSITION": [],
    "FINANCIAL ASSISTANCE": [
        "General",
        "Medical Care & Hospital bills",
        "Prescription Medication"
    ],
    "FIRST EPISODE PSYCHOSIS (FEP)": [],
    "GRIEF SUPPORT": [
        "For Children & Teens",
        "Loss from Suicide",
        "Support Services"
    ],
    "GUN VIOLENCE PREVENTION": [],
    "HEALTH INSURANCE PORTABILITY & ACCOUNTABILITY ACT (HIPAA)": [],
    "HOARDING": [],
    "HOUSING": [
        "Discrimination & Complaints",
        "Eviction",
        "Resources"
    ],
    "INCARCERATED PERSONS": [
        "Appealing Sentence",
        "Mistreatment While Incarcerated",
        "Reentry After a Period of Incarceration",
        "Resources"
    ],
    "INSURANCE": [
        "Coverage & Complaints",
        "Mental Health Parity"
    ],
    "INTELLECTUAL DISABILITIES": [],
    "INTERNATIONAL MENTAL HEALTH RESOURCES": [],
    "INVOLUNTARY & CIVIL COMMITMENT": [],
    "IMMIGRATED & UNDOCUMENTED PERSONS": [],
    "LATINX COMMUNITY": [],
    "LAW ENFORCEMENT COMMUNITY": [],
    "LEGAL": [
        "Low-cost/Pro Bono (free) Services",
        "Fee-based Representation",
        "Guardianship & Conservatorship",
        "Psychiatric Advance Directives"
    ],
    "LGBTQI COMMUNITY": [
        "Legal",
        "Resources",
        "Transgender-Specific"
    ],
    "LONG COVID RESOURCES": [],
    "LONG-TERM CARE PLANNING": [],
    "MEDICATION": [
        "Prescription Medication Financial Assistance",
        "Resources"
    ],
    "MISSING PERSONS": [],
    "MUSLIM AMERICAN COMMUNITY": [],
    "NATIVE AMERICAN/INDIGENOUS COMMUNITY": [],
    "OBSESSIVE-COMPULSIVE DISORDER (OCD)": [],
    "OPPOSITIONAL DEFIANT DISORDER (ODD)": [],
    "PEER SUPPORT SERVICES": [],
    "PERSONALITY DISORDERS": [
        "Borderline Personality Disorder",
        "Narcissistic Personality Disorder"
    ],
    "PHYSICAL DISABILITY": [],
    "POST-TRAUMATIC STRESS DISORDER (PTSD)": [],
    "PSYCHOSIS": [],
    "RELATIONSHIPS": [
        "Family",
        "Friendship",
        "Romantic"
    ],
    "REPRODUCTIVE HEALTH RELATED - MENTAL HEALTH": [],
    "RESEARCH – MENTAL HEALTH": [
        "Finding Current Research",
        "Participating in Research",
        "Research Funding"
    ],
    "SCHIZOPHRENIA SPECTRUM & OTHER PSYCHOTIC DISORDERS": [],
    "SCHOLARSHIPS & GRANTS": [],
    "SELF-INJURY": [],
    "SLEEP DISORDERS": [],
    "SOCIAL & LOCAL SERVICES": [],
    "STATISTICS": [],
    "SUBSTANCE RELATED & ADDICTIVE DISORDERS": [
        "Alcohol",
        "Compulsive Sexual Behavior",
        "Dual Diagnosis",
        "Gambling",
        "Internet & Gaming",
        "Narcotics",
        "Resources"
    ],
    "SUICIDE": [
        "Crisis",
        "Support Groups for Suicidal Ideation & Loss From Suicide",
        "Supporting Someone with Suicidal Thoughts"
    ],
    "TRANSPORTATION": [
        "Aging Populations",
        "Resources"
    ],
    "TRAUMA": [],
    "TREATMENT": [
        "Affordable Treatment (No Insurance or Public Insurance)",
        "Alternative Treatments",
        "HealthCare & Frontline Workers",
        "Online and Telemental Health",
        "Private Insurance",
        "Psychiatrists",
        "Psychotherapy/Talk Therapy",
        "Psychologists",
        "Treatment Facilities",
        "Treatment Facility Accrediting Agencies"
    ],
    "VETERANS/MILITARY": [
        "Crisis",
        "Legal",
        "Resources"
    ]
}
data = None
with open ('newdata.txt', 'r') as file:
    data = json.load(file)
print(len(data))
simpledata = []
client = OpenAI()
num = 327

#should be: for resource in data
for i in range (546):
    try:
        result = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
        messages=[
            {"role": "user", "content": f"I'm providing you with a text description of a mental health service and its relevant hyperlinks. I would like you to ONLY return a structured list of dictionaries in JSON of: the provider of the service (or name), email, phone number, video, website; the general_category of the service and the sub_category (in two different keys), extract the category from this python dictionary {table_of_contents}. Where the keys are the general categories and the values are the subcategories, if you are unsure about the subcategory, assign a null value; and a short description of the service; and the hyperlinks that I provided you (do not access these links, the list should be made based only on the text I provide). Here is the text and links: {data[i+326]}." }
        #+ 'Additionally, here’s an example of what your return should look like. Example: Text: NAMI ADHD & Bipolar: Signs at a Young Age Video Tessa Brooks shares her mentalhealth journey as a child and young adult experiencing early signs of ADHD and bipolardisorder. Learn about her journey to find an accurate diagnosis, recovery, support andchosen family in the NAMI community. Hyperlinks Attached: https://youtu.be/J5v4gQ_io1Y. Example Output: [{"provider": "NAMI","email": None, "phone": None, "website": None, "video": "https://youtu.be/J5v4gQ_io1Y", "category": "ADHD","links": "https://youtu.be/J5v4gQ_io1Y", "short_description": "Tessa Brooks shares her mental health journey as a young person experiencing signs of ADHD and bi-polar disorder"}]'
        ]    
        )
        newres = json.loads(result.choices[0].message.content)
        #print(newres["provider"])
        simpledata.append(newres)
        with open ('finaldata.txt', 'w') as file:
            json.dump(simpledata, file)
        print('ran once and number:', num)
        num += 1
        time.sleep(0.2)
    except Exception as e:
        print(e)
        with open ('errors.txt', 'a') as file:
            file.write(f"THIS IS WHAT FAILED AAAAHAHAHAHAHAHAHAHAHAHAH: {num}")
            file.write(result.choices[0].message.content)
    
print(simpledata)
with open ('finaldata.txt', 'w') as file:
            json.dump(simpledata, file)




