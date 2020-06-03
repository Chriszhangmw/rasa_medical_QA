## story_1_search_treat_simple    <!-- name of the story - just for debugging -->
* greet
   - utter_greet
* search_treat{"disease": "百日咳"}
   - action_search_treat
* bye
   - utter_goodbye

## story_2_search_food_simple
* greet
   - utter_greet
* search_food{"disease": "百日咳"}
   - action_search_food
* bye
   - utter_goodbye

## story_3_search_symptom_simple
* greet
   - utter_greet
* search_symptom{"disease": "百日咳"}
   - action_search_symptom
* bye
   - utter_goodbye

## story_4_search_cause_simple
* greet
   - utter_greet
* search_cause{"disease": "百日咳"}
   - action_search_cause
* bye
   - utter_goodbye

## story_5_search_neopathy_simple
* greet
   - utter_greet
* search_neopathy{"disease": "百日咳"}
   - action_search_neopathy
* bye
   - utter_goodbye

## story_6_search_drug_simple
* greet
   - utter_greet
* search_drug{"disease": "百日咳"}
   - action_search_drug
* bye
   - utter_goodbye

## story_7_search_prevention_simple
* greet
   - utter_greet
* search_prevention{"disease": "百日咳"}
   - action_search_prevention
* bye
   - utter_goodbye

## story_8_search_drug_func_simple
* greet
   - utter_greet
* search_drug_func{"drug": "头孢地尼分散片"}
   - action_search_drug_func
* bye
   - utter_goodbye

## story_9_search_disease_treat_time_simple
* greet
   - utter_greet
* search_disease_treat_time{"disease": "百日咳"}
   - action_search_disease_treat_time
* bye
   - utter_goodbye

## story_10_search_easy_get_simple
* greet
   - utter_greet
* search_easy_get{"disease": "百日咳"}
   - action_search_easy_get
* bye
   - utter_goodbye

## story_11_search_disease_dept_simple
* greet
   - utter_greet
* search_disease_dept{"disease": "百日咳"}
   - action_search_disease_dept
* bye
   - utter_goodbye

## story_120
* first
   - utter_greet

## story_12
* greet
   - utter_greet
   
## story_13
* bye
   - utter_goodbye

## story_14
* search_treat{"disease": "过敏性皮炎"}
   - action_search_treat
   
## story_15
* search_food{"disease": "过敏性皮炎"}
   - action_search_food
   
## story_16
* search_symptom{"disease": "过敏性皮炎"}
   - action_search_symptom
   
## story_17
* search_cause{"disease": "过敏性皮炎"}
   - action_search_cause
   
## story_18
* search_neopathy{"disease": "过敏性皮炎"}
   - action_search_neopathy
   
## story_19
* search_drug{"disease": "过敏性皮炎"}
   - action_search_drug
   
## story_20
* search_prevention{"disease": "过敏性皮炎"}
   - action_search_prevention
   
## story_21
* search_drug_func{"drug": "复方斑蝥胶囊"}
   - action_search_drug_func
   
## story_22
* search_disease_treat_time{"disease": "过敏性皮炎"}
   - action_search_disease_treat_time
   
## story_23
* search_easy_get{"disease": "过敏性皮炎"}
   - action_search_easy_get
   
## story_24
* search_disease_dept{"disease": "过敏性皮炎"}
   - action_search_disease_dept
   
## form_story_1
* request_professor_diagnosis
   - diagnosis_form
   - form{"name":"diagnosis_form"}
   - slot{"request_slot":"symptom"}
* form: inform{"symptom":"肺外症状"}
   - form:diagnosis_form
   - slot{"symptom":"肺外症状"}
   - slot{"request_slot":"drug"}
* form: inform{"drug":"司帕沙星片"}
   - form: diagnosis_form
   - slot{"drug":"司帕沙星片"}
   - slot{"request_slot":"disease"}
* diagnosis_form{"disease":"大叶性肺炎"}
   - form{"name":"diagnosis_form"}
   - slot{"disease":"大叶性肺炎"}
   - form:{"name":null}
   - slot{"requested_slot":null}
* bye
   - utter_goodbye
   
## form_story_1
* request_professor_diagnosis
   - diagnosis_form
   - form{"name":"diagnosis_form"}
   - slot{"request_slot":"symptom"}
* form: inform{"symptom":"劳累后遗精"}
   - form:diagnosis_form
   - slot{"symptom":"劳累后遗精"}
   - slot{"request_slot":"drug"}
* form: inform{"drug":"加味逍遥丸"}
   - form: diagnosis_form
   - slot{"drug":"加味逍遥丸"}
   - slot{"request_slot":"disease"}
* diagnosis_form{"disease":"肺念珠菌病"}
   - form{"name":"diagnosis_form"}
   - slot{"disease":"肺念珠菌病"}
   - form:{"name":null}
   - slot{"requested_slot":null}
* bye
   - utter_goodbye
  
## form_story_1
* request_professor_diagnosis
   - diagnosis_form
   - form{"name":"diagnosis_form"}
   - slot{"request_slot":"symptom"}
* form: inform{"symptom":"足跟痛"}
   - form:diagnosis_form
   - slot{"symptom":"足跟痛"}
   - slot{"request_slot":"drug"}
* form: inform{"drug":"达沙替尼片"}
   - form: diagnosis_form
   - slot{"drug":"达沙替尼片"}
   - slot{"request_slot":"disease"}
* diagnosis_form{"disease":"鼾症"}
   - form{"name":"diagnosis_form"}
   - slot{"disease":"鼾症"}
   - form:{"name":null}
   - slot{"requested_slot":null}
* bye
   - utter_goodbye