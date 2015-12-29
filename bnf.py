'''
copy/paste of the bnf taxonomy on https://openprescribing.net/bnf/
plus some simple code to provide lookups through two functions

- path - returns a list of chapter, section, paragraph
- description - returns a string version of the path (concatenated with '|')


According to http://www.evidence.nhs.uk/formulary/bnf/current/ :

BNF Code:
The BNF Code is a 15 digit code in which the first seven digits are allocated according to the categories in the BNF and the last 8 digits represent the medicinal product, form, strength and the link to the generic equivalent product. The digits in the code represent the following information:

- 1 & 2     BNF Chapter
- 3 & 4     BNF Section
- 5 & 6     BNF Paragraph
- 7      BNF Sub-Paragraph
- 8 & 9     Chemical substance
- 10 & 11      Product
- 12 & 13      Strength / Formulation
- 14 & 15      Link to the generic equivalent product.  A is used when there is no linking record.

'''

bnf_='''1: Gastro-Intestinal System
   1.1: Dyspep&Gastro-Oesophageal Reflux Disease
      1.1.1: Antacids and Simeticone
      1.1.2: Compound Alginates&Prop Indigestion Prep
   1.2: Antispasmod.&Other Drgs Alt.Gut Motility
   1.3: Antisecretory Drugs+Mucosal Protectants
      1.3.1: H2-Receptor Antagonists
      1.3.2: Selective Antimuscarinics
      1.3.3: Chelates And Complexes
      1.3.4: Prostaglandin Analogues
      1.3.5: Proton Pump Inhibitors
      1.3.6: Other Antisec Drugs+Mucosal Protectants
   1.4: Acute Diarrhoea
      1.4.1: Adsorbents And Bulk-Forming Drugs
      1.4.2: Antimotility Drugs
      1.4.3: Enkephalinase Inhibitors
   1.5: Chronic Bowel Disorders
      1.5.1: Aminosalicylates
      1.5.2: Corticosteroids
      1.5.3: Drugs Affecting Immune Response
      1.5.4: Food Allergy
   1.6: Laxatives
      1.6.1: Bulk-Forming Laxatives
      1.6.2: Stimulant Laxatives
      1.6.3: Faecal Softeners
      1.6.4: Osmotic Laxatives
      1.6.5: Bowel Cleansing Preparations
      1.6.6: Peripheral Opioid-Receptor Antagonists
      1.6.7: Other Drugs Used In Constipation
   1.7: Local Prepn for Anal & Rectal Disorders
      1.7.1: Soothing Haemorrhoidal Preparations
      1.7.2: Co Haemorrhoidal Prep's + Corticosteroid
      1.7.3: Rectal Sclerosants
      1.7.4: Management of Anal Fissures
   1.8: Stoma Care
      1.8.1: Local Care of Stoma
   1.9: Drugs Affecting Intestinal Secretions
      1.9.1: Drugs Affecting Biliary Composition&Flow
      1.9.2: Bile Acid Sequestrants
      1.9.4: Pancreatin
2: Cardiovascular System
   2.1: Positive Inotropic Drugs
      2.1.1: Cardiac Glycosides
      2.1.2: Phosphodiesterase Type-3 Inhibitors
   2.2: Diuretics
      2.2.1: Thiazides And Related Diuretics
      2.2.2: Loop Diuretics
      2.2.3: Pot-Sparing Diuretics&Aldosterone Antag
      2.2.4: Potassium Sparing Diuretics & Compounds
      2.2.5: Osmotic Diuretics
      2.2.8: Diuretics With Potassium
   2.3: Anti-Arrhythmic Drugs
      2.3.2: Drugs For Arrhythmias
   2.4: Beta-Adrenoceptor Blocking Drugs
   2.5: Hypertension and Heart Failure
      2.5.1: Vasodilator Antihypertensive Drugs
      2.5.2: Centrally-Acting Antihypertensive Drugs
      2.5.3: Adrenergic Neurone Blocking Drugs
      2.5.4: Alpha-Adrenoceptor Blocking Drugs
      2.5.5: Renin-Angiotensin System Drugs
      2.5.6: Ganglion-Blocking Drugs
      2.5.8: Other Adrenergic Neurone Blocking Drugs
   2.6: Nit,Calc Block & Other Antianginal Drugs
      2.6.1: Nitrates
      2.6.2: Calcium-Channel Blockers
      2.6.3: Other Antianginal Drugs
      2.6.4: Peripheral Vasodilators & Related Drugs
      2.6.5: Flosequinan
      2.6.10: Other Vasodilators for Angina
   2.7: Sympathomimetics
      2.7.1: Inotropic Sympathomimetics
      2.7.2: Vasoconstrictor Sympathomimetics
      2.7.3: Cardiopulmonary Resuscitation
   2.8: Anticoagulants And Protamine
      2.8.1: Parenteral Anticoagulants
      2.8.2: Oral Anticoagulants
      2.8.3: Protamine Sulfate
   2.9: Antiplatelet Drugs
   2.10: Stable Angina, Acute/Crnry Synd&Fibrin
      2.10.2: Fibrinolytic Drugs
   2.11: Antifibrinolytic Drugs & Haemostatics
   2.12: Lipid-Regulating Drugs
   2.13: Local Sclerosants
3: Respiratory System
   3.1: Bronchodilators
      3.1.1: Adrenoceptor Agonists
      3.1.2: Antimuscarinic Bronchodilators
      3.1.3: Theophylline
      3.1.4: Compound Bronchodilator Preparations
   3.2: Corticosteroids (Respiratory)
   3.3: Cromoglycate,Rel,Leukotriene Antagonists
      3.3.1: Cromoglycate and Related Therapy
      3.3.2: Leukotriene Receptor Antagonists
      3.3.3: Phosphodiesterase Type-4 Inhibitors
   3.4: Antihist, Hyposensit & Allergic Emergen
      3.4.1: Antihistamines
      3.4.2: Allergen Immunotherapy
      3.4.3: Allergic Emergencies
   3.5: Resp Stimulants & Pulmonary Surfactants
      3.5.1: Respiratory Stimulants
   3.6: Oxygen
   3.7: Mucolytics
   3.8: Aromatic Inhalations
   3.9: Cough Preparations
      3.9.1: Cough Suppressants
      3.9.2: Expectorant & Demulcent Cough Prep's
   3.10: Systemic Nasal Decongestants
   3.11: Antifibrotics
      3.11.1: Antifibrotics
4: Central Nervous System
   4.1: Hypnotics And Anxiolytics
      4.1.1: Hypnotics
      4.1.2: Anxiolytics
      4.1.3: Barbiturates
   4.2: Drugs Used In Psychoses & Rel.Disorders
      4.2.1: Antipsychotic Drugs
      4.2.2: Antipsychotic Depot Injections
      4.2.3: Drugs Used for Mania and Hypomania
   4.3: Antidepressant Drugs
      4.3.1: Tricyclic & Related Antidepressant Drugs
      4.3.2: Monoamine-Oxidase Inhibitors (Maois)
      4.3.3: Selective Serotonin Re-Uptake Inhibitors
      4.3.4: Other Antidepressant Drugs
   4.4: CNS Stimulants and drugs used for ADHD
   4.5: Drugs used in the Treatment of Obesity
      4.5.1: Gastro-Intestinal Anti-Obesity Drugs
      4.5.2: Centrally-Acting Appetite Suppressants
   4.6: Drugs Used In Nausea And Vertigo
   4.7: Analgesics
      4.7.1: Non-Opioid Analgesics And Compound Prep
      4.7.2: Opioid Analgesics
      4.7.3: Neuropathic Pain
      4.7.4: Antimigraine Drugs
   4.8: Antiepileptics
      4.8.1: Control Of Epilepsy
      4.8.2: Drugs Used In Status Epilepticus
   4.9: Drugs Used In Park'ism/Related Disorders
      4.9.1: Dopaminergic Drugs Used In Parkinsonism
      4.9.2: Antimuscarinic Drugs Used In Parkin'ism
      4.9.3: Essentialtremor,Chorea,Tics&Reldisorders
   4.10: Drugs Used In Substance Dependence
      4.10.1: Alcohol Dependence
      4.10.2: Nicotine Dependence
      4.10.3: Opioid Dependence
   4.11: Drugs for Dementia
5: Infections
   5.1: Antibacterial Drugs
      5.1.1: Penicillins
      5.1.2: Cephalosporins and other Beta-Lactams
      5.1.3: Tetracyclines
      5.1.4: Aminoglycosides
      5.1.5: Macrolides
      5.1.6: Clindamycin and Lincomycin
      5.1.7: Some Other Antibiotics
      5.1.8: Sulfonamides And Trimethoprim
      5.1.9: Antituberculosis Drugs
      5.1.10: Antileprotic Drugs
      5.1.11: Metronidazole, Tinidazole & Ornidazole
      5.1.12: Quinolones
      5.1.13: Urinary-Tract Infections
   5.2: Antifungal Drugs
      5.2.1: Triazole Antifungals
      5.2.2: Imidazole Antifungals
      5.2.3: Polyene Antifungals
      5.2.4: Echinocandin Antifungals
      5.2.5: Other Antifungals
   5.3: Antiviral Drugs
      5.3.1: HIV Infection
      5.3.2: Herpesvirus Infections
      5.3.3: Viral Hepatitis
      5.3.4: Influenza
      5.3.5: Respiratory Syncytial Virus
   5.4: Antiprotozoal Drugs
      5.4.1: Antimalarials
      5.4.2: Amoebicides
      5.4.3: Trichomonacides
      5.4.4: Antigiardial Drugs
      5.4.5: Leishmaniacides
      5.4.8: Drugs For Pneumocystis Pneumonia
   5.5: Anthelmintics
      5.5.1: Drugs For Threadworms
      5.5.2: Ascaricides
      5.5.3: Drugs For Tapeworm Infections
      5.5.4: Drugs For Hookworms
      5.5.5: Schistosomicides
      5.5.6: Filaricides
      5.5.8: Drugs For Strongyloidiasis
6: Endocrine System
   6.1: Drugs Used In Diabetes
      6.1.1: Insulin
      6.1.2: Antidiabetic Drugs
      6.1.4: Treatment Of Hypoglycaemia
      6.1.5: Diabetic Nephropathy & Neuropathy
      6.1.6: Diabetic Diagnostic & Monitoring Agents
   6.2: Thyroid And Antithyroid Drugs
      6.2.1: Thyroid Hormones
      6.2.2: Antithyroid Drugs
   6.3: Corticosteroids (Endocrine)
      6.3.1: Replacement Therapy
      6.3.2: Glucocorticoid Therapy
   6.4: Sex Hormones
      6.4.1: Female Sex Hormones & Their Modulators
      6.4.2: Male Sex Hormones And Antagonists
      6.4.3: Anabolic Steroids
   6.5: Hypothalamic&Pituitary Hormones&Antioest
      6.5.1: Hypothalamic&Ant Pituit Hormone&Antioest
      6.5.2: Posterior Pituitary Hormones&Antagonists
   6.6: Drugs Affecting Bone Metabolism
      6.6.1: Calcitonin and Parathyroid Hormone
      6.6.2: Bisphosphonates and Other Drugs
   6.7: Other Endocrine Drugs
      6.7.1: Bromocriptine & Other Dopaminergic Drugs
      6.7.2: Drugs affecting Gonadotrophins
      6.7.3: Metyrapone
      6.7.4: Somatomedins
7: Obstetrics,Gynae+Urinary Tract Disorders
   7.1: Drugs Used In Obstetrics
      7.1.1: Prostaglandins And Oxytocics
      7.1.2: Mifepristone
      7.1.3: Myometrial Relaxants
   7.2: Treatment Of Vaginal & Vulval Conditions
      7.2.1: Preparations For Vaginal/Vulval Changes
      7.2.2: Vaginal and Vulval Infections
   7.3: Contraceptives
      7.3.1: Combined Hormonal Contraceptives/Systems
      7.3.2: Progestogen-only Contraceptives
      7.3.3: Spermicidal Contraceptives
      7.3.5: Emergency Contraception
   7.4: Drugs For Genito-Urinary Disorders
      7.4.1: Drugs For Urinary Retention
      7.4.2: Drugs/Urin'y Frequ'cy Enuresis & Incont
      7.4.3: Drugs Used In Urological Pain
      7.4.4: Bladder Instillations/Urological Surgery
      7.4.5: Drugs For Erectile Dysfunction
      7.4.6: Drugs For Premature Ejaculation
8: Malignant Disease & Immunosuppression
   8.1: Cytotoxic Drugs
      8.1.1: Alkylating Drugs
      8.1.2: Anthracyclines & Cytotoxic Antibiotics
      8.1.3: Antimetabolites
      8.1.4: Vinca Alkaloids And Etoposide
      8.1.5: Other Antineoplastic Drugs
   8.2: Drugs Affecting The Immune Response
      8.2.1: Antiproliferative Immunosuppressants
      8.2.2: Cortico'oids & Other Immunosuppressants
      8.2.3: Anti-lymphocyte Monoclonal Antibodies
      8.2.4: Other Immunomodulating Drugs
   8.3: Sex Hormones & Antag In Malig Disease
      8.3.1: Oestrogens
      8.3.2: Progestogens
      8.3.3: Androgens
      8.3.4: Hormone Antagonists
9: Nutrition And Blood
   9.1: Anaemias + Other Blood Disorders
      9.1.1: Iron-Deficiency Anaemias
      9.1.2: Drugs used in Megaloblastic Anaemias
      9.1.3: Hypoplastic/Haemolytic & Renal Anaemias
      9.1.4: Drugs used in Platelet Disorders
      9.1.6: Drugs used in Neutropenia
      9.1.7: Drugs used to Mobilise Stem Cells
   9.2: Fluids And Electrolytes
      9.2.1: Oral Prepn for Fluid & Electrolyte Imb
      9.2.2: Parent Prepn for Fluid & Electrolyte Imb
   9.3: Intravenous Nutrition
   9.4: Oral Nutrition
      9.4.1: Foods For Special Diets
      9.4.2: Enteral Nutrition
   9.5: Minerals
      9.5.1: Calcium And Magnesium
      9.5.2: Phosphorus
      9.5.3: Fluoride
      9.5.4: Zinc & other Minerals
      9.5.5: Selenium
   9.6: Vitamins
      9.6.1: Vitamin A
      9.6.2: Vitamin B Group
      9.6.3: Vitamin C
      9.6.4: Vitamin D
      9.6.5: Vitamin E
      9.6.6: Vitamin K
      9.6.7: Multivitamin Preparations
      9.6.8: Other Vitamin Formulations
   9.7: Bitters And Tonics
   9.8: Metabolic Disorders
      9.8.1: Drugs Used in Metabolic Disorders
      9.8.2: Acute Porphyrias
   9.9: Foods
   9.10: Compound Vit/Mineral Formulations
   9.11: Health Supplements
      9.11.1: Amino Acids & Nutritional Agents
      9.11.2: Enzymes
      9.11.3: Glandular
      9.11.4: Digestive Aids
   9.12: Other Health Supplements
10: Musculoskeletal & Joint Diseases
   10.1: Drugs Used In Rheumatic Diseases & Gout
      10.1.1: Non-Steroidal Anti-Inflammatory Drugs
      10.1.2: Corticosteroids
      10.1.3: Rheumatic Disease Suppressant Drugs
      10.1.4: Gout & Cytotoxic Induced Hyperuicaemia
      10.1.5: Other Drugs For Rheumatic Diseases
   10.2: Drugs Used In Neuromuscular Disorders
      10.2.1: Dgs Which Enhance Neuromus'ar Transmi'on
      10.2.2: Skeletal Muscle Relaxants
   10.3: Soft-Tissue Disorders & Topical Pain Rel
      10.3.1: Enzymes
      10.3.2: Rubefacients,Top NSAIDS,Capsaicin & Poul
11: Eye
   11.3: Anti-Infective Eye Preparations
      11.3.1: Antibacterials
      11.3.2: Antifungals
      11.3.3: Antivirals
   11.4: Corti'roids & Other Anti-Inflamm.Preps.
      11.4.1: Corticosteroids
      11.4.2: Other Anti-Inflammatory Preparations
   11.5: Mydriatics And Cycloplegics
   11.6: Treatment Of Glaucoma
   11.7: Local Anaesthetics
   11.8: Miscellaneous Ophthalmic Preparations
      11.8.1: Tear Deficiency,Eye Lubricant/Astringent
      11.8.2: Ocular Diagnos/Peri-op Prepn&Photodyn Tt
      11.8.3: Other Eye Preparations
      11.8.5: Preparations for Cataracts
   11.9: Contact Lenses
12: Ear, Nose And Oropharynx
   12.1: Drugs Acting On The Ear
      12.1.1: Otitis Externa
      12.1.2: Otitis Media
      12.1.3: Removal of Ear Wax & other Substances
   12.2: Drugs Acting On The Nose
      12.2.1: Drugs Used In Nasal Allergy
      12.2.2: Topical Nasal Decongestants
      12.2.3: Nasal Prepn for Infection
   12.3: Drugs Acting On The Oropharynx
      12.3.1: Drugs For Oral Ulceration & Inflammation
      12.3.2: Oropharyngeal Anti-Infective Drugs
      12.3.3: Lozenges & Sprays
      12.3.4: Mouth-Washes, Gargles, And Dentifrices
      12.3.5: Treatment Of Dry Mouth
13: Skin
   13.1: Vehicles & Emulsifying Agents
      13.1.1: Vehicles & Emulsifying Agents
   13.2: Emollient & Barrier Preparations
      13.2.1: Emollients
      13.2.2: Barrier Preparations
      13.2.3: Dusting-Powders
   13.3: Top Local Anaesthetics & Antipruritics
   13.4: Topical Corticosteroids
   13.5: Preparations For Eczema And Psoriasis
      13.5.1: Preparations For Eczema
      13.5.2: Preparations For Psoriasis
      13.5.3: Drugs Affecting The Immune Response
   13.6: Acne and Rosacea
      13.6.1: Topical Preparations For Acne
      13.6.2: Oral Preparations For Acne
      13.6.3: Topical Preparation For Rosacea
   13.7: Preparations For Warts And Calluses
   13.8: Sunscreens And Camouflagers
      13.8.1: Sunscreening Preparations
      13.8.2: Camouflagers
   13.9: Shampoo&Other Preps For Scalp&Hair Cond
   13.10: Anti-Infective Skin Preparations
      13.10.1: Antibacterial Preparations
      13.10.2: Antifungal Preparations
      13.10.3: Antiviral Preparations
      13.10.4: Parasiticidal Preparations
      13.10.5: Prep's For Minor Cuts & Abrasions
   13.11: Skin Cleansers,Antiseptics & Desloughing
      13.11.1: Alcohols & Saline
      13.11.2: Chlorhexidine Salts
      13.11.3: Cationic Surfactants & Soaps
      13.11.4: Chlorine & Iodine
      13.11.5: Phenolics
      13.11.6: Oxidisers & Dyes
      13.11.7: Desloughing Agents
   13.12: Antiperspirants
   13.13: Wound Management Products
      13.13.1: Medicated Stockings
      13.13.2: Surgical Adhesive Removers
      13.13.8: Gel And Colloid Dressings
   13.14: Topical Circulatory Preparations
   13.15: Miscellaneous Topical Preparations
14: Immunological Products & Vaccines
   14.3: Diagnostic Vaccines
   14.4: Vaccines And Antisera
   14.5: Immunoglobulins
      14.5.1: Normal Immunoglobulin
      14.5.2: Disease-Specific Immunoglobulins
      14.5.3: Anti-D (Rho) Immunoglobulin
15: Anaesthesia
   15.1: General Anaesthesia
      15.1.1: Intravenous Anaesthetics
      15.1.2: Inhalational Anaesthetics
      15.1.3: Antimuscarinic Drugs
      15.1.4: Sedative & Analgesic Peri-Operative Drgs
      15.1.5: Neuromuscular Blocking Drugs
      15.1.6: Anticholinesterases Used in Anaesthesia
      15.1.7: Antagonists for Respiratory Depression
      15.1.8: Drugs for Malignant Hyperthermia
   15.2: Local Anaesthesia
      15.2.1: Local Anaesthetics
      15.2.2: Adjuncts To Intractable Pain Spasticity
18: Preparations used in Diagnosis
   18.1: Urine Testing Reagents
   18.3: X-Ray Contrast Media
   18.4: Diagnostic Agents
   18.5: Special Sanction Reagents
19: Other Drugs And Preparations
   19.1: Alcohol, Wines & Spirits
   19.2: Selective Preparations
      19.2.1: Individually Formulated Preps-Bought In
      19.2.2: Individ Formulated Preps-Prepared Extemp
      19.2.3: Homeopathic Preparations
      19.2.5: Household & Other Over The Counter Lines
      19.2.7: Poisoning Antidotes
   19.3: Adjuncts To Dispensing
   19.4: Single Substances
   19.5: Other Preparations
   19.6: Acids
      19.6.1: Concentrated Waters
      19.6.2: Essences
      19.6.3: Extracts
      19.6.4: Infusions
      19.6.5: Oils
      19.6.6: Tinctures
      19.6.7: Syrups
   19.7: Base/Dil/Susp Agents/Stabilisers
   19.8: Colouring,Flavouring & Sweetening Agents
   19.9: Disinfectants,Preserv&Sterilising Agents
   19.10: Polysorbates & Tween
   19.11: Lubricating Jellies/Pessaries
   19.12: Electrode/Ultrasonic Gels
   19.13: Cordials/Soft Drinks
   19.14: Waters
      19.14.1: Sterile Water
      19.14.2: Purified Water
      19.14.3: Tap Water
      19.14.4: Spring/Mineral & Soda Waters
   19.15: Other Gases
20: Dressings
   20.1: Absorbent Cottons
   20.2: Arm Sling/Bandages
   20.3: Wound Management & other Dressings
   20.4: Gauzes & Gauze Tissue
   20.5: Tracheostomy & Laryngectomy Appliances
   20.6: Foam
   20.7: Lints
   20.8: Plasters
   20.9: Stockinette
   20.10: Surgical Adhesive Tape
   20.11: Surgical Sutures
   20.12: Swabs
   20.13: Unspecified Dressing
   20.14: Skin Closure Strips, Sterile
   20.15: Skin Adhesive,Sterile
   20.16: Tapeless Holders
   20.17: Cervical Collar
   20.18: Cellulose Wadding BP 1988
   20.20: Silk Garments
21: Appliances
   21.1: Other Appliances
   21.2: Catheters
   21.3: Chiropody Appliances
   21.4: Contraceptive Devices
   21.5: Suprapubic Appliances
   21.6: Trusses
   21.7: Elastic Hosiery
   21.8: Oxygen Masks
   21.9: Special Sanction Authorisations
   21.10: C.A.P.D. Administration Equipment
   21.11: Special Authorisation Guernsey
   21.12: Peak Flow Meters
   21.13: Catheter Maintenance Solutions
   21.14: Lubricant Gels
   21.16: Irrigation Solutions
   21.17: Nasal Device
   21.18: Vacuum Pumps for Erectile Dysfunction
   21.19: Oral Film Forming Agents
   21.20: Venous Ulcer Compression System
   21.21: Dry Mouth Products
   21.22: Emollients
   21.23: Vaginal Moisturisers
   21.24: Nasal Products
   21.25: Vaginal Dilators
   21.26: Leg Ulcer Wrap
   21.27: Lymphoedema Garments
   21.28: Anal Irrigation System
   21.29: Plantar Pressure Offloading Device
   21.30: Eye Products
   21.31: Cycloidal Vibration Accessories
   21.32: Inhalation Solutions
   21.33: Indwelling Pleural Cath Drain System
   21.34: Vaginal PH Correction Products
   21.35: Acne Treatment
   21.36: Adhesive Dressing Remover Ster Silicone
   21.37: Pelvic Toning Devices
   21.38: Low Friction Products
   21.39: Prosthetic Adhesives
   21.40: Bacterial Decolonisation Products
   21.41: Physical Debridement Device
   21.42: Jaw Rehabilitation Device
   21.43: Micro-Enema - Sodium Citrate
   21.44: Dev For Adjunctive Tt Of Hypertension
   21.45: Douches
   21.46: Hernia Support Garments
22: Incontinence Appliances
   22.2: Anal Plugs
   22.5: Catheter Valves
   22.10: Drainable Dribbling Appliances
   22.15: Faecal Collectors
   22.20: Incontinence Belts
   22.30: Incontinence Sheaths
   22.40: Incontinence Sheath Fixing Strips & Adh
   22.50: Leg Bags
   22.60: Night Drainage Bags
   22.70: Suspensory Systems
   22.80: Tubing And Accessories
   22.85: Insert For Female Stress Incont
   22.90: Urinal Systems
23: Stoma Appliances
   23.5: Adhesive Discs/Rings/Pads/Plasters
   23.10: Adhesive (Pastes/Sprays/Solutions)
   23.15: Adhesive Removers (Sprays/Liquids/Wipes)
   23.20: Bag Closures
   23.25: Bag Covers
   23.30: Belts
   23.35: Colostomy Bags
   23.40: Colostomy Sets
   23.45: Deodorants
   23.46: Discharge Solidifying Agents
   23.50: Filters/Bridges
   23.55: Flanges
   23.60: Ileostomy Bags
   23.65: Ileostomy Sets
   23.70: Irrigation Washout Appliances
   23.75: Pressure Plates/Shields
   23.80: Skin Fillers And Protectives
   23.85: Skin Protectors
   23.90: Stoma Caps/Dressings
   23.92: Tubing & Accessories
   23.93: Accessories (Guernsey)
   23.94: Two Piece Ostomy Systems
   23.96: Urostomy Bags
   23.98: Urostomy Sets
   23.99: Ostomy Appliances R/Sub Allowed Pre 1985'''

bnfdict_=dict()
for i in bnf_.split('\n'):
    section,sep,desc=i.partition(':')
    bnfdict_[section.strip()]=desc.strip()

def path(x):
    #coords=map(lambda y: y.lstrip('0'),(x[:2],x[2:4],x[4:6],x[6:7]))
    coords=map(lambda y: y.lstrip('0'),(x[:2],x[2:4],x[4:6]))
    path=list()
    result=list()
    for coord in coords:
        if not len(coord):
            break
        path.append(coord)
        try:
            k='.'.join(path)
            result.append(bnfdict_[k])
        except:
            #print x
            return result #give as much as we can
    return result

def description(x):
   return ' | '.join(path(x))