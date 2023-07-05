
# ------ META PROMPTS ------ #

# Inital system prompt given to ChatGPT
META_PROMPT = """
	You are a machine that is responsible for processing telephone call transcripts between salespeople and potential customers. You will be given an overview of a product disclosure statement and a transcript of a phone call
    and will need to determine if the salesperson has made any promises or claims that do not align with the product disclosure statement. The transcript will follow the structure of the conversation with any sentences said by
    the salesperson being prefaced by "SALESPERSON" and similarly any sentences said by the potential customer being prefaced by "CUSTOMER:". The PDS may contain some information that is not able to be shared with you, this 
    information will be replaced by "(REDACTED)" and should be ignored by you. If you do detect any variance in what is said from the product disclosure statement, you will respond by saying "POTENTIAL BREACH" followed by the 
    reasoning for why you believe that there has been a variance by the salesperson. If you do not detect any variance you will respond with "COMPLIANT".
"""

# ------ PDSs ------ #

PDS_1 = """
	This PDS is for a car insurance policy which covers the policyholder from any third party liabilities in the case that they have an accident while driving. The policy does not include cover for the driver's vehicle only 
    third-party damage caused in the incident. The product includes a premium of $100 paid monthly by the user to the insurance company and has a lock in period of 2 years. If the customer decides that they wish to exit the 
    contract early they will have to pay an exit fee equivalent to two months of premiums. If by the end of the two years, the user has not made any claims they will be refunded half of the premiums they paid.
"""

PDS_2 = """
	This PDS is for a life insurance policy which provides a payout in the case of death equal to their age multipled by 1,000 up until the age of 95. However, in the case that the individual dies between the ages of 70 and 80
    not inclusive they will receive an additional $10,000 on top of their base payout. The policy holder will be charged a monthly premium $120 from when they first take the policy out until they reach an age of 95 at which point
    they will be refunded all of their premiums paid. A special discount is if the user is under the age of 35 when they first take the policy out they will only have to pay a monthly premium of $100 instead of $120, however if th
    policy holder lapses on their payments while having this discount and then at a latter stage they take the policy out once again after they have surpassed the age of 35 this discount will still apply.
"""

# ------ TRANSCRIPTS ------ #

TEST_TRANSCRIPT_1 = """
	CUSTOMER: Hello, (REDACTED) speaking?
    SALESPERSON: Hello (REDACTED). This is (REDACTED) calling from car insurance 101 about your recent inquiry into out third part car insurance policy.
    CUSTOMER: Oh yes, hi (REDACTED) I say an advertisment for the policy on my way to work and saw that it included a good no claims discounts and wanted to learn about it.
    SALESPERSON: Great, well the policy covers any third party damage that may occur excluding any damage to your car if you have an accident and lasts for two years. The discount you saw would have been that if you do not make any claims during the two years you receive half of the premium you paid back.
    CUSTOMER: Yes, that is the one I was looking at. One detail I wasn't sure on though was what the monthly premiums were and if there were any penalties for ending the policy early?
    SALESPERSON: Ok, well we charge a flat $100 premiums paid monthly which is in line with our competitors and do not charge any additional fees if you decide to cancel to policy early.
    CUSTOMER: Oh wow that sounds like a great deal. 
"""

TEST_TRANSCRIPT_2 = """
	CUSTOMER: Hello, (REDACTED) speaking?
    SALESPERSON: Hello (REDACTED). This is (REDACTED) calling from car insurance 101 about your recent inquiry into out third part car insurance policy.
    CUSTOMER: Oh yes, hi (REDACTED) I say an advertisment for the policy on my way to work and saw that it included a good no claims discounts and wanted to learn about it.
    SALESPERSON: Great, well the policy covers any third party damage that may occur excluding any damage to your car if you have an accident and lasts for two years. The discount you saw would have been referring to the fee refund that if you do not make any claims during the two years you receive half of the premium you paid back.
    CUSTOMER: Yes, that is the one I was looking at. One detail I wasn't sure on though was what the monthly premiums were and if there were any penalties for ending the policy early?
    SALESPERSON: Ok, well we charge a flat $100 premiums paid monthly which is in line with our competitors and there is a early cancellation fee equal to two months of premiums.
    CUSTOMER: Oh wow that sounds like a great deal. Could you do me a special deal where I only pay $80 a month?
    SALESPERSON: Unfortunately I'm not allowed to apply individual discounts to customers, so the lowest I can offer you is the rate of $100 a month
"""

TEST_TRANSCRIPT_3 = """
	CUSTOMER: Hello, I'm (REDACTED). I'm calling as I wish to take out a life insurance policy.
    SALESPERSON: Hello (REDACTED). That's great thanks for choosing us to provide you with this policy. Before we can proceed I will first need to ask you some questions.
    CUSTOMER: Ok, sounds good.
    SALESPERSON: Would you mind providing me with your age?
    CUSTOMER: I am 56
    SALESPERSON: Thank you, now as you are 56 you are not applicable to the youth discount and as such your monthly premiums will be $120.
    CUSTOMER: Oh, I thought that as I had this policy previously while under the age of 35 that I would still be eligible for the discount?
    SALESPERSON: Sorry (REDACTED) but that is incorrect. You can only receive the youth discount if you are under the age of 35 when you first take out the policy.
    CUSTOMER: Oh, that is disappointing I must have mis remembered the terms of the product. I'd like to proceed anyway.
"""

TEST_TRANSCRIPT_4 = """
	CUSTOMER: Hello, I'm (REDACTED). I'm calling as I wish to take out a life insurance policy.
    SALESPERSON: Hello (REDACTED). That's great thanks for choosing us to provide you with this policy. Before we can proceed I will first need to ask you some questions.
    CUSTOMER: Ok, sounds good.
    SALESPERSON: Would you mide providing me with your age?
    CUSTOMER: I am 56
    SALESPERSON: Thank you, now as you are 56 you are not applicable to the youth discount and as such your monthly premiums will be $120.
    CUSTOMER: Oh, I thought that as I had this policy previously while under the age of 35 that I would still be eligible for the discount?
    SALESPERSON: Sorry (REDACTED) but that is incorrect. You can only receive the youth discount if you are under the age of 35 when you first take out the policy.
    CUSTOMER: Oh, that is disappointing I must have misremembered the terms of the product. Would you mind checking with in the PDS for me?
    SALESPERSON: Yes certainly .... Oh it appears I was mistaken you actually are applicable for the youth discount apologies for my mistake
    CUSTOMER: No worries, in that case I'd like to continue and take out this policy.
"""