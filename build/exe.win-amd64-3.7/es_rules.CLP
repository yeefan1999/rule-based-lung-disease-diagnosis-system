
;; the template of the personal information
(deftemplate person
   (slot name)
   (slot age)
   (slot gender))

;; Rule 1
(defrule option-asthma
(choose option-one)
=>
(assert (ques1 chest-tightness))
(assert (ques2 wheezing)))

;; Rule 2
(defrule symptoms-asthma
(ques1 yes)
(ques2 yes)
(choose option-one)
=>
(assert (symptoms-of-asthma))
(assert (intro Asthma-makes-breathing-difficult.There-is-no-cure,-but-it-can-be-treated-to-live-a-normal-and-healthy-life.)))

;; Rule 3
(defrule asthma
(symptoms-of-asthma)
=>
(assert (disease asthma)))

;; Rule 4
(defrule asthma-symptoms
(disease asthma)
=>
(assert (treatment Medicine Regular-healthcare Clinical-trials Omalizumab Mepolizumab-Reslizumab-and-Benralizumab Bronchial-thermoplasty))
(assert (diagnosis Doctor-will-evaluate-the-symptoms-you-have,-provided-with-your-health-history.The-doctor-will-conduct-a-physical-exam-and-look-at-the-test-results.))
(assert (causes Genetics Allergies Respiratories-infections Environment Smoking Air-pollution Obesity)))

;; Rule 5
(defrule option-pneumothorax
(choose option-two)
=>
(assert (ques1 shortness-of-breath))
(assert (ques2 dry-cough)))

;; Rule 6
(defrule symptoms-pneumothorax
(ques1 yes)
(ques2 yes)
(choose option-two)
=>
(assert (symptoms-of-pneumothorax))
(assert (intro Also-called-as-collapsed-lung,-it-occurs-when-air-leaks-into-the-space-between-lung-and-chest-wall.The-pressure-from-the-air-push-on-the-lung-to-give-way.Lung-collapse-prevents-the-lung-from-expanding-when-inhailing.)))

;; Rule 7
(defrule pneumothorax
(symptoms-of-pneumothorax)
=>
(assert (disease pneumothorax)))

;; Rule 8
(defrule pneumothorax-symptoms
(disease pneumothorax)
=>
(assert (treatment Needle-aspiration Chest-tube Surgery))
(assert (diagnosis Doctor-will-listen-to-your-chest-through-a-stethoscope.Doctor-may-suggest-an-arterial-blood-gas-test.Doctor-will-need-to-order-an-imaging-test-such-as-CT-scan-for-accurate-diagnosis.))
(assert (causes Chest-injury Lung-disease Rupture-air-blisters Mechanical-ventilation Smoking Genetics Previous-penumothorax)))

;; Rule 9
(defrule option-bronchiolitis
(choose option-three)
=>
(assert (ques1 fever-/-stuffy-nose))
(assert (ques2 frequent-cough)))

;; Rule 10
(defrule symptoms-bronchiolitis
(ques1 yes)
(ques2 yes)
(choose option-three)
=>
(assert (symptoms-of-bronchiolitis))
(assert (intro Bronchiolitis-develops-when-small-airways-in-the-lungs-become-injured.The-easy--passage-of-air-is-blocked-and-cause-shortness-of-breath-and-cough.)))

;; Rule 11
(defrule bronchiolitis
(symptoms-of-bronchiolitis)
=>
(assert (disease bronchiolitis)))

;; Rule 12
(defrule bronchiolitis-symptoms
(disease bronchiolitis)
=>
(assert (treatment Emergency-care Symptomatic-care Monitoring Fever-control Nose-drops-or-spray Encourgae-fluids))
(assert (diagnosis Doctor-will-start-with-a-basic-physical-exam.A-chest-Xray-may-be-needed.A-blood-test-may-be-needed-to-check-for-the-sign-of-infection))
(assert (causes Premature-birth Depressed-immune-system Never-have-breast-fed Environment Virus-infections)))

;; Rule 13
(defrule option-copd
(choose option-four)
=>
(assert (ques1 shortness-of-breath))
(assert (ques2 erspiratory-infections)))	

;; Rule 14
(defrule symptoms-copd
(ques1 yes)
(ques2 yes)
(choose option-four)
=>
(assert (symptoms-of-copd))
(assert (intro COPD-is-a-chronic-disease-that-can-cause-serious-long-term-disability-and-early-death.There-is-no-cure-for-COPD,-but-it-is-preventable-and-treatable.)))

;; Rule 15
(defrule copd
(symptoms-of-copd)
=>
(assert (disease chronic-obstructive-pulmonary-disease)))

;; Rule 16
(defrule copd-symptoms
(disease chronic-obstructive-pulmonary-disease)
=>
(assert (treatment Pulmonary-rehabilitation Supplemental-oxygen Surgery Clinical-Trials Conplementary-therapies Palliative-care))
(assert (diagnosis Spirometry-and-other-tests))
(assert (causes Smoking Environment Genetic)))

;; Rule 17
(defrule option-cancer
(choose option-five)
=>
(assert (ques1 hoarseness))
(assert (ques2 frequent-lung-infections)))

;; Rule 18
(defrule symptoms-cancer
(ques1 yes)
(ques2 yes)
(choose option-five)
=>
(assert (symptoms-of-cancer))
(assert (intro Lung-cancer-occurs-when-cells-in-the-lung-mutate.There-are-many-factors-cause-this-mutation.)))

;; Rule 19
(defrule cancer
(symptoms-of-cancer)
=>
(assert (disease lung-cancer)))

;; Rule 20
(defrule cancer-symptoms
(disease lung-cancer)
=>
(assert (treatment Surgery Radiation-therapy Chemotherapy Targeted-therapy Immunotherapy Clinical-trials Palliative-care))
(assert (diagnosis It-can-be-diagnosed-through-imaging-test,-sputum-cytology,-tissue-sample-and-biopsy))
(assert (causes Smoking Radon Hazardous-chemicals Particle-pollution Genes)))

;; Rule 21
(defrule disease_option_asthma
(choose_disease option-one)
=>
(assert (disease_symptoms Chest-tightness Shortness-of-breath Frequent-cough Wheezing)))

;; Rule 22
(defrule disease_option_pneumothorax
(choose_disease option-two)
=>
(assert (disease_symptoms Sharp/-stabbing-chest-pain Shortness-of-breath Bluish-skin Rapid-breathing Dry-cough)))

;; Rule 23
(defrule disease_option_bronchiolitis
(choose_disease option-three)
=>
(assert (disease_symptoms Common-cold Runny-nose Fever-/-Stuffy-nose Loss-of-appetite Frequent-cough Wheezing)))

;; Rule 24
(defrule disease_option_copd
(choose_disease option-four)
=>
(assert (disease_symptoms Chronic-cough Shortness-of-cbreath Respiratory-infections Fatigue Cyanosis/-Bluish-skin Wheezing)))

;; Rule 25
(defrule disease_option_cancer
(choose_disease option-five)
=>
(assert (disease_symptoms Hoarseness Chest-pain Shortness-of-breath Blood-coughing Frequent-lung-infections Frequent-cough)))

;; Rule 26
(defrule disease_result_one
(disease_result option-one)
=>
(assert (choose option-one))
(assert (ques1 yes)))

;; Rule 27
(defrule disease_result_two
(disease_result option-two)
=>
(assert (choose option-two))
(assert (ques1 yes)))

;; Rule 28
(defrule disease_result_three
(disease_result option-three)
=>
(assert (choose option-three))
(assert (ques1 yes)))

;; Rule 29
(defrule disease_result_four
(disease_result option-four)
=>
(assert (choose option-four))
(assert (ques1 yes)))

;; Rule 30
(defrule disease_result_five
(disease_result option-five)
=>
(assert (choose option-five))
(assert (ques1 yes)))