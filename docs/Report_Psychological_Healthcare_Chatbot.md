# **Development of a Psychological Healthcare Chatbot Expert System**  🤖

## **Team:** 👥
* Diana Lorena Balanta Solano
* Carlos Javier Bolaños Riascos.
* Danna Alexandra Espinosa Arenas

## **Introduction**

In today's digital era, access to mental health services remains a significant challenge for many individuals. Factors such as social stigma, high costs, and limited availability of professional resources hinder many from obtaining the necessary help. In response to this issue, the development of expert systems based on chatbots offers an innovative and accessible solution. These chatbots can provide a confidential and easily accessible platform for receiving psychological support, guidance, and resources.

This project focuses on developing a medium-complexity expert system chatbot for psychological healthcare using Python and the Experta and pgmpy libraries. The system is designed to offer personalized, evidence-based support to users experiencing psychological distress or seeking mental health guidance, utilizing Bayesian networks to model probabilistic relationships between symptoms, diagnoses, and treatment recommendations.

## **Problem Statement and Objectives**


### **Problem Statement:**
Accessing mental health services is a significant challenge due to various barriers, including social stigma, high costs, and limited availability of qualified professionals. These barriers prevent many individuals from receiving the necessary help and support, leading to the worsening of untreated mental health issues.

### **Objectives:**
The main objective of this project is to develop a medium-complexity expert system chatbot for psychological healthcare using Python and the Experta and pgmpy libraries. The specific objectives are:

* Provide an accessible and confidential platform for users to receive psychological support and guidance.

* Utilize Bayesian networks to model and evaluate the probabilistic relationships between symptoms, diagnoses, and treatment recommendations.

* Develop a chatbot that can interact conversationally with users, assessing their psychological state and providing appropriate responses based on expert knowledge.

* Validate the chatbot's accuracy and effectiveness through usability testing and validation against established psychological principles.

* Ensure the system complies with privacy regulations and ethical guidelines regarding user data and confidentiality.

### **Definition of the Scope of the Problem**

The chatbot will function similarly to a psychologist, starting with a greeting and asking how the user is doing and if they would like to share anything, always ensuring that the conversation is confidential. The system will identify the reason for the consultation without asking directly and will paraphrase what the user shares, providing a brief summary. It will offer strategies and tools useful in moments of crisis, words of support, and will work with issues that are solvable by the user, avoiding topics beyond its scope. This interaction will be based on user information, conversation, and generated recommendations.

### **Identification of Users**

The primary users of this system will be:

* Students at Universidad Icesi who need psychological support.

* Collaborators and administrative staff at Universidad Icesi seeking mental health assistance.

* The University Welfare Department, which will use the system to provide quick and early support for the emotional problems of the Icesista community.


### **System Benefits**

The expert system chatbot for psychological assistance will provide the following benefits:

1. **Accessibility:** It will facilitate access to psychological support services at any time and from anywhere.

2. **Confidentiality:** It will offer a safe and confidential environment for users to express their problems without fear of stigma.

3. **Early Intervention:** It will help detect and manage emotional problems early, preventing the worsening of conditions.

4. **Continuous Support:** It will provide ongoing resources and coping strategies to improve users' mental health and well-being.

5. **Ease of Use**: A user-friendly interface that facilitates interaction and access to the necessary help.

###  **Feasibility Test**

### **Technical:**
We evaluated the capabilities of Python libraries, especially Experta for expert systems logic, and others like Pandas for data management. This evaluation included the installation and testing of each library to ensure adequate compatibility and functionality.

We also reviewed the documentation of each tool to ensure sufficient support and usage examples that facilitate learning and implementation.

### **Financial:**
We confirmed that all necessary resources are free and open-source, suitable for academic use without incurring additional costs. This also includes verifying that no additional hardware investments are required, using personal equipment that meets the minimum software requirements.

### **Operational:**
We verified the compatibility of these tools with the operating system of the personal computer to be used and ensured that sufficient time is available within the semester to complete the project, considering other academic responsibilities.


## **Requirements Analysis**



### **Functional Requirements:**

* **Chatbot Interaction:**

  * The chatbot must be able to interact conversationally with users.

  * It should assess user input to identify specific psychological issues.

  * The system should generate responses and recommendations based on the assessments made.

* **Knowledge Base:**

  * The system should have a knowledge base that includes psychological assessments, coping strategies, and intervention techniques.

  * The knowledge base must be updatable and expandable.

* **Bayesian Networks:**

  * The system must use Bayesian networks to model probabilistic relationships between symptoms, diagnoses, and treatment recommendations.

  * The Bayesian networks should be implemented using the pgmpy library.

* **Data Storage:**

  * A database should exist to store user profiles, conversation logs, and relevant psychological data.

  * The database must ensure the security and confidentiality of user data.

* **Explanation Facilities:**

  * The system should provide clear explanations of the chatbot's reasoning and recommendations.

  * Explanations should be accessible to users to increase trust and understanding.

### **Non-Functional Requirements:**

* **Usability:**

  * The chatbot must be easy to use and accessible to users from diverse demographics.

  * The interface should be intuitive and user-friendly.

* **Performance:**

  * The system must handle multiple user sessions simultaneously without performance degradation.

  * It should be scalable to support an increasing number of users.

* **Security and Privacy:**

  * The system must comply with all applicable privacy regulations and ensure user data confidentiality.

  * Robust security measures should be implemented to protect sensitive information.

* **Maintainability:**

  * The system should be easily maintainable and updatable.

  * Documentation should be clear and comprehensive to facilitate future improvements and maintenance.

##  **Knowledge Base**


### 1. **Anxiety**

**Strategies:**

  * Breathing Techniques: Teach deep breathing exercises to reduce anxiety.

  * Mindfulness and Meditation: Guide users through mindfulness and meditation exercises.

  * Cognitive Behavioral Therapy (CBT): Provide techniques for cognitive restructuring to change negative thoughts.

  * Progressive Muscle Relaxation: Instruct users in practicing progressive muscle relaxation.

### 2. **Depression**
**Strategies:**

* Behavioral Activation: Suggest enjoyable and meaningful activities to improve mood.
* Cognitive Behavioral Therapy (CBT): Help identify and change negative thought patterns.
* Social Support: Encourage connection with friends and family.
* Self-care: Promote healthy habits such as exercise, balanced diet, and adequate sleep.

### 3. **Stress**

**Strategies:**

  * Relaxation Techniques: Teach relaxation techniques like meditation and deep breathing.

  * Time Management: Provide advice on organizing and prioritizing tasks.

  * Mindfulness: Introduce mindfulness practices to stay present in the moment.

  * Recreational Activities: Suggest recreational activities to relieve stress.

### 4. **Post-Traumatic Stress Disorder (PTSD)**
**Strategies:**

  * Exposure Therapy: Guide the user through gradual exposure to traumatic memories (under professional supervision).

  * Cognitive Therapy: Help change thoughts and beliefs related to the trauma.

  * Mindfulness and Relaxation: Provide techniques to reduce hypervigilance and anxiety.

### 5. **Sleep Problems**
**Strategies:**

  * Sleep Hygiene: Suggest healthy bedtime routines and create a conducive sleep environment.

  * Cognitive Behavioral Therapy for Insomnia (CBT-I): Provide techniques to change negative thoughts about sleep.

  * Relaxation and Meditation: Teach relaxation and meditation techniques to improve sleep quality.

### 6. **Anger Management**
**Strategies:**

  * Relaxation Techniques: Teach breathing and relaxation techniques to calm down.

  * Cognitive Restructuring: Help change negative thoughts that trigger anger.

  * Problem-Solving: Provide strategies to address situations that provoke anger constructively.

  * Physical Exercise: Suggest exercise as a way to release accumulated tension.

### 7.  **Low Self-Esteem**

**Strategies:**

  * Cognitive Behavioral Therapy (CBT): Help identify and change negative self-thoughts.

  * Positive Affirmations: Promote the use of positive affirmations to improve self-image.

  * Goal Setting: Guide in creating realistic and achievable goals to build confidence.

  * Social Support: Encourage seeking support and positive feedback from friends and family.

### **Resources Used**

World Health Organization (WHO): Guides and documents on mental health and intervention strategies.
APA Handbook of Clinical Psychology: Manuals and resources from the APA providing evidence-based techniques and strategies.

## **System Design**

### **Knowledge Base Modeling**


* Description: The knowledge base contains all the information necessary for the chatbot, including psychological assessments, coping strategies, and intervention techniques.

* Structure: The knowledge base will be structured into specific categories.

#### 2. **Outline of the Rules(Inference engine)**

Below is an outline of the rules that will define the system logic, based on the knowledge base:


#### **Rules with Bayesian Probabilities**

1. **Anxiety**
   - **Rule 1**: If the user reports anxiety symptoms, there is a high probability that they need deep breathing techniques.
   - **Rule 2**: If symptoms persist and are severe, there is a high probability that the user will benefit from Cognitive Behavioral Therapy (CBT).
   - **Rule 3**: Combining mindfulness and relaxation techniques has a medium probability of improving mild anxiety.

2. **Depression**
   - **Rule 1**: If the user reports symptoms of depression, there is a high probability that behavioral activation will improve their mood.
   - **Rule 2**: If the user experiences persistent negative thoughts, CBT has a high probability of being effective.
   - **Rule 3**: Social support and enjoyable activities have a medium probability of improving moderate depression.

3. **Stress**
   - **Rule 1**: If the user reports high levels of stress, there is a high probability that relaxation techniques and meditation will be effective.
   - **Rule 2**: Time management and recreational activities have a medium probability of reducing moderate stress.

4. **Post-Traumatic Stress Disorder (PTSD)**
   - **Rule 1**: If the user reports symptoms of PTSD, there is a high probability that gradual exposure will be effective under professional supervision.
   - **Rule 2**: Cognitive therapy has a high probability of helping change trauma-related thoughts.

5. **Sleep Problems**
   - **Rule 1**: If the user reports sleep problems, there is a high probability that sleep hygiene practices will be effective.
   - **Rule 2**: CBT-I has a high probability of being effective in changing negative thoughts about sleep.
   - **Rule 3**: Relaxation and meditation techniques have a medium probability of improving sleep quality.

6. **Anger Management**
   - **Rule 1**: If the user reports anger management issues, there is a high probability that breathing and relaxation techniques will be effective.
   - **Rule 2**: Cognitive restructuring has a high probability of being effective in changing negative thoughts.
   - **Rule 3**: Physical exercise has a medium probability of helping release accumulated tension.

7. **Low Self-Esteem**
   - **Rule 1**: If the user reports low self-esteem, there is a high probability that CBT will be effective in changing negative thoughts.
   - **Rule 2**: Positive affirmations have a medium probability of improving self-image.
   - **Rule 3**: Setting realistic goals has a high probability of boosting confidence.

#### **Bayesian Network for Each Problem**

#### 1. Bayesian Network for Anxiety

- **Nodes**:
  - **Anxiety Symptoms**: (yes/no)
  - **Anxiety Diagnosis**: (mild/moderate/severe)
  - **Coping Strategies**: (breathing/mindfulness/CBT)
  - **Treatment Effectiveness**: (high/medium/low)

- **Relationships**:
  - Anxiety Symptoms -> Anxiety Diagnosis
  - Anxiety Diagnosis -> Coping Strategies
  - Coping Strategies -> Treatment Effectiveness

#### 2. Bayesian Network for Depression
- **Nodes:**

  - **Depression Symptoms**: (yes/no)
  - **Depression Diagnosis**: (mild/moderate/severe)
  - **Coping Strategies**: (behavioral activation/CBT/social support)
  - **Treatment Effectiveness**: (high/medium/low)

- **Relationships:**

  - Depression Symptoms -> Depression Diagnosis
  - Depression Diagnosis -> Coping Strategies
  - Coping Strategies -> Treatment Effectiveness

#### 3. Bayesian Network for Stress
- **Nodes:**

  - **Stress Symptoms**: (yes/no)
  - **Stress Diagnosis**: (mild/moderate/severe)
  - **Coping Strategies**: (relaxation/time management/recreation)
  - **Treatment Effectiveness**: (high/medium/low)

- **Relationships:**

  - Stress Symptoms -> Stress Diagnosis
  - Stress Diagnosis -> Coping Strategies
  - Coping Strategies -> Treatment Effectiveness

#### 4. Bayesian Network for Post-Traumatic Stress Disorder (PTSD)
- **Nodes:**

  - **PTSD Symptoms**: (yes/no)
  - **PTSD Diagnosis**: (mild/moderate/severe)
  - **Coping Strategies**: (gradual exposure/cognitive therapy/mindfulness)
  - **Treatment Effectiveness**: (high/medium/low)

**Relationships:**

  - PTSD Symptoms -> PTSD Diagnosis
  - PTSD Diagnosis -> Coping Strategies
  - Coping Strategies -> Treatment Effectiveness

#### 5. Bayesian Network for Sleep Problems
- **Nodes:**

  - **Sleep Problems**: (yes/no)
  - **Sleep Diagnosis**: (mild/moderate/severe)
  - **Coping Strategies**: (sleep hygiene/CBT-I/relaxation)
  - **Treatment Effectiveness**: (high/medium/low)

**Relationships:**

  - Sleep Problems -> Sleep Diagnosis
  - Sleep Diagnosis -> Coping Strategies
  - Coping Strategies -> Treatment Effectiveness


#### 6. Bayesian Network for Anger Management
**Nodes:**

  - **Anger Symptoms**: (yes/no)
  - **Anger Diagnosis**: (mild/moderate/severe)
  - **Coping Strategies**: (breathing/relaxation/cognitive restructuring)
  - **Treatment Effectiveness**: (high/medium/low)

**Relationships:**

  - Anger Symptoms -> Anger Diagnosis
  - Anger Diagnosis -> Coping Strategies
  - Coping Strategies -> Treatment Effectiveness

#### 7. Bayesian Network for Low Self-Esteem
**Nodes:**

  - **Low Self-Esteem Symptoms**: (yes/no)
  - **Self-Esteem Diagnosis**: (mild/moderate/severe)
  - **Coping Strategies**: (CBT/positive affirmations/goal setting)
  - **Treatment Effectiveness**: (high/medium/low)

**Relationships:**

  - Low Self-Esteem Symptoms -> Self-Esteem Diagnosis
  - Self-Esteem Diagnosis -> Coping Strategies
  - Coping Strategies -> Treatment Effectiveness

