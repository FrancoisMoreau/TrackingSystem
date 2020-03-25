#!/usr/bin/python
# -*- coding: latin-1 -*-

DOCUMENT_TYPE = [('not_sel', 'Not Selected'),
                 ('degree_plan', 'Degree Plan'),
                 ('annual_review', 'Annual Review'),
                 ('other', 'Other')]

DEGREE_PLAN_DOC_TYPE = [('not_sel', 'Not Selected'),
                        ('deg_plan', 'Degree Plan'),
                        ('P_change_commitee', 'Petition for change of committee'),
                        ('P_course_change', 'Petition for course change'),
                        ('P_extension_of_time_limits', 'Petition for extension of time limits'),
                        ('P_waivers_of_exceptions', 'Petition for waivers of exceptions'),
                        ('mdd', 'MDD'),
                        ('other', 'Other')]

PRE_EXAM_DOC_TYPE = [('not_sel', 'Not Selected'),
                     ('checklist', 'Preliminary Exam Checklist'),
                     ('report', 'Preliminary Exam Report'),
                     ('written', 'Preliminary Exam Written')]

QUAL_EXAM_DOC_TYPE = [('not_sel', 'Not Selected'),
                      ('qual_exam', 'Qualifying Exam'),
                      ('other', 'Other')]

ANNUAL_REVIEW_DOC_TYPE = [('not_sel', 'Not Selected'),
                      ('annual_review', 'Annual Review'),
                      ('other', 'Other')]

ANNUAL_REVIEW_STATUS_TYPE = [('none', '----'),
                             ('sat', 'Satisfied'),
                             ('need_imp', 'Need Improvement'),
                             ('unsat', 'Unsatisfied')]

T_D_PROP_DOC_TYPE = [('not_sel', 'Not Selected'),
                     ('title_page', 'Thesis/Dissertation Proposal Title Page'),
                     ('prop', 'Thesis/Dissertation Proposal')]

T_D_DOC_TYPE = [('not_sel', 'Not Selected'),
                ('approval', 'Thesis/Dissertation Approval Page'),
                ('t_d', 'Thesis/Dissertation')]

FIN_EXAM_DOC_TYPE = [('not_sel', 'Not Selected'),
                     ('request', 'Request for Final Examination'),
                     ('req_for_exemp', 'Request for exemption from Final Examination'),
                     ('report', 'Report of Final Exam')]

GENDER = [('not_ans', 'Prefer Not to Answer'),
          ('male', 'Male'),
          ('female', 'Female'),
          ('trans', 'Transgender')]

ETHNICITY_TYPE = [('unknown', 'Unknown'),
                  ('african_ame', 'Black/African American'),
                  ('asian', 'Asian'),
                  ('white', 'White'),
                  ('his_or_la', 'Hispanic or Latino'),
                  ('island', 'Native Hawaiian or Pacific Islander'),
                  ('international', 'International'),
                  ('not_ans', 'Prefer Not to Answer')]

STUDENT_STATUS_TYPE = [('current', 'Current'),
                       ('graduated', 'Gradudated'),
                       ('invalid', 'Invalid')]

DEGREE_TYPE = [('m_thesis', 'Masters(Thesis)'),
               ('m_non_thesis', 'Masters(Non-Thesis)'),
               ('phd', 'PhD'),
               ('non_degree', 'Non-Degree')]

SEMESTER_TYPE = [('fall', 'Fall'),
                 ('spring', 'Spring'),
                 ('summer', 'Summer')]

EXAM_RESULT_TYPE = [('none', '----'),
                 ('pass', 'Pass'),
                 ('fail', 'Fail')]

YES_NO_TYPE = [('yes', 'Yes'),
               ('no', 'No')]

MAJOR_TYPE = [('cpsc', 'CPSC'),
              ('cecn', 'CECN'),
              ('en', 'EN'),
              ('comp', 'COMP'),
              ]

US_RESIDENCY_TYPE = [('usa', 'USA'),
                     ('usc', 'USC - U.S. Citizen'),
                     ('usfr', 'USPR - U.S. Permanent Resident'),
                     ('nra', 'NRA - Non Resident Alien / International'),
                     ('u', 'U - Unknown')]

TEXAS_RESIDENCY_TYPE = [('r', 'R - Resident'),
                        ('t', 'T - Resident, Not State Funded'),
                        ('u', 'U - Resident, Not State Funded, 7 Year'),
                        ('n', 'N - Non-Resident'),
                        ('p', 'P - Non-Resident, Not State Funded, 7 Year'),
                        ('i', 'I - International'),
                        ('k', 'K - International, Not State Funded, 7 Year'),
                        ('j', 'J - International, Not State Funded'),
                        ('w', 'W - SB1502, Not State Funded, 7 Year'),
                        ('v', 'V - SB1520, Not State Funded'),
                        ('h', 'H - SZASSTD'),
                        ('s', 'S - Unknown')]

CITIZENSHIP = [
    ("AF", "Afghanistan - Islamic Republic of Afghanistan"),
    ("AL", "Albania - Republic of Albania"),
    ("DZ", "Algeria - People's Democratic Republic of Algeria"),
    ("AS", "American Samoa"),
    ("AD", "Andorra - Principality of Andorra"),
    ("AO", "Angola - Republic of Angola"),
    ("AI", "Anguilla"),
    ("AQ", "Antarctica"),
    ("AG", "Antigua and Barbuda"),
    ("AR", "Argentina - Argentine Republic"),
    ("AM", "Armenia - Republic of Armenia"),
    ("AW", "Aruba"),
    ("AU", "Australia"),
    ("AT", "Austria - Republic of Austria"),
    ("AZ", "Azerbaijan - Republic of Azerbaijan"),
    ("BS", "Bahamas - Commonwealth of the Bahamas"),
    ("BH", "Bahrain - Kingdom of Bahrain"),
    ("BD", "Bangladesh - People's Republic of Bangladesh"),
    ("BB", "Barbados"),
    ("BY", "Belarus - Republic of Belarus"),
    ("BE", "Belgium - Kingdom of Belgium"),
    ("BZ", "Belize"),
    ("BJ", "Benin - Republic of Benin"),
    ("BM", "Bermuda"),
    ("BT", "Bhutan - Kingdom of Bhutan"),
    ("BO", "Bolivia, Plurinational State of - Plurinational State of Bolivia"),
    ("BQ", "Bonaire, Sint Eustatius and Saba - Bonaire, Sint Eustatius and Saba"),
    ("BA", "Bosnia and Herzegovina - Republic of Bosnia and Herzegovina"),
    ("BW", "Botswana - Republic of Botswana"),
    ("BV", "Bouvet Island"),
    ("BR", "Brazil - Federative Republic of Brazil"),
    ("IO", "British Indian Ocean Territory"),
    ("BN", "Brunei Darussalam"),
    ("BG", "Bulgaria - Republic of Bulgaria"),
    ("BF", "Burkina Faso"),
    ("BI", "Burundi - Republic of Burundi"),
    ("CV", "Cabo Verde - Republic of Cabo Verde"),
    ("KH", "Cambodia - Kingdom of Cambodia"),
    ("CM", "Cameroon - Republic of Cameroon"),
    ("CA", "Canada"),
    ("KY", "Cayman Islands"),
    ("CF", "Central African Republic"),
    ("TD", "Chad - Republic of Chad"),
    ("CL", "Chile - Republic of Chile"),
    ("CN", "China - People's Republic of China"),
    ("CX", "Christmas Island"),
    ("CC", "Cocos (Keeling) Islands"),
    ("CO", "Colombia - Republic of Colombia"),
    ("KM", "Comoros - Union of the Comoros"),
    ("CG", "Congo - Republic of the Congo"),
    ("CD", "Congo, The Democratic Republic of the"),
    ("CK", "Cook Islands"),
    ("CR", "Costa Rica - Republic of Costa Rica"),
    ("HR", "Croatia - Republic of Croatia"),
    ("CU", "Cuba - Republic of Cuba"),
    ("CW", "Curaçao - Curaçao"),
    ("CY", "Cyprus - Republic of Cyprus"),
    ("CZ", "Czechia - Czech Republic"),
    ("CI", "Côte d'Ivoire - Republic of Côte d'Ivoire"),
    ("DK", "Denmark - Kingdom of Denmark"),
    ("DJ", "Djibouti - Republic of Djibouti"),
    ("DM", "Dominica - Commonwealth of Dominica"),
    ("DO", "Dominican Republic"),
    ("EC", "Ecuador - Republic of Ecuador"),
    ("EG", "Egypt - Arab Republic of Egypt"),
    ("SV", "El Salvador - Republic of El Salvador"),
    ("GQ", "Equatorial Guinea - Republic of Equatorial Guinea"),
    ("ER", "Eritrea - the State of Eritrea"),
    ("EE", "Estonia - Republic of Estonia"),
    ("SZ", "Eswatini - Kingdom of Eswatini"),
    ("ET", "Ethiopia - Federal Democratic Republic of Ethiopia"),
    ("FK", "Falkland Islands (Malvinas)"),
    ("FO", "Faroe Islands"),
    ("FJ", "Fiji - Republic of Fiji"),
    ("FI", "Finland - Republic of Finland"),
    ("FR", "France - French Republic"),
    ("GF", "French Guiana"),
    ("PF", "French Polynesia"),
    ("TF", "French Southern Territories"),
    ("GA", "Gabon - Gabonese Republic"),
    ("GM", "Gambia - Republic of the Gambia"),
    ("GE", "Georgia"),
    ("DE", "Germany - Federal Republic of Germany"),
    ("GH", "Ghana - Republic of Ghana"),
    ("GI", "Gibraltar"),
    ("GR", "Greece - Hellenic Republic"),
    ("GL", "Greenland"),
    ("GD", "Grenada"),
    ("GP", "Guadeloupe"),
    ("GU", "Guam"),
    ("GT", "Guatemala - Republic of Guatemala"),
    ("GG", "Guernsey"),
    ("GN", "Guinea - Republic of Guinea"),
    ("GW", "Guinea-Bissau - Republic of Guinea-Bissau"),
    ("GY", "Guyana - Republic of Guyana"),
    ("HT", "Haiti - Republic of Haiti"),
    ("HM", "Heard Island and McDonald Islands"),
    ("VA", "Holy See (Vatican City State)"),
    ("HN", "Honduras - Republic of Honduras"),
    ("HK", "Hong Kong - Hong Kong Special Administrative Region of China"),
    ("HU", "Hungary - Hungary"),
    ("IS", "Iceland - Republic of Iceland"),
    ("IN", "India - Republic of India"),
    ("ID", "Indonesia - Republic of Indonesia"),
    ("IR", "Iran, Islamic Republic of - Islamic Republic of Iran"),
    ("IQ", "Iraq - Republic of Iraq"),
    ("IE", "Ireland"),
    ("IM", "Isle of Man"),
    ("IL", "Israel - State of Israel"),
    ("IT", "Italy - Italian Republic"),
    ("JM", "Jamaica"),
    ("JP", "Japan"),
    ("JE", "Jersey"),
    ("JO", "Jordan - Hashemite Kingdom of Jordan"),
    ("KZ", "Kazakhstan - Republic of Kazakhstan"),
    ("KE", "Kenya - Republic of Kenya"),
    ("KI", "Kiribati - Republic of Kiribati"),
    ("KP", "Korea, Democratic People's Republic of - Democratic People's Republic of Korea"),
    ("KR", "Korea, Republic of"),
    ("KW", "Kuwait - State of Kuwait"),
    ("KG", "Kyrgyzstan - Kyrgyz Republic"),
    ("LA", "Lao People's Democratic Republic"),
    ("LV", "Latvia - Republic of Latvia"),
    ("LB", "Lebanon - Lebanese Republic"),
    ("LS", "Lesotho - Kingdom of Lesotho"),
    ("LR", "Liberia - Republic of Liberia"),
    ("LY", "Libya - Libya"),
    ("LI", "Liechtenstein - Principality of Liechtenstein"),
    ("LT", "Lithuania - Republic of Lithuania"),
    ("LU", "Luxembourg - Grand Duchy of Luxembourg"),
    ("MO", "Macao - Macao Special Administrative Region of China"),
    ("MG", "Madagascar - Republic of Madagascar"),
    ("MW", "Malawi - Republic of Malawi"),
    ("MY", "Malaysia"),
    ("MV", "Maldives - Republic of Maldives"),
    ("ML", "Mali - Republic of Mali"),
    ("MT", "Malta - Republic of Malta"),
    ("MH", "Marshall Islands - Republic of the Marshall Islands"),
    ("MQ", "Martinique"),
    ("MR", "Mauritania - Islamic Republic of Mauritania"),
    ("MU", "Mauritius - Republic of Mauritius"),
    ("YT", "Mayotte"),
    ("MX", "Mexico - United Mexican States"),
    ("FM", "Micronesia, Federated States of - Federated States of Micronesia"),
    ("MD", "Moldova, Republic of - Republic of Moldova"),
    ("MC", "Monaco - Principality of Monaco"),
    ("MN", "Mongolia"),
    ("ME", "Montenegro - Montenegro"),
    ("MS", "Montserrat"),
    ("MA", "Morocco - Kingdom of Morocco"),
    ("MZ", "Mozambique - Republic of Mozambique"),
    ("MM", "Myanmar - Republic of Myanmar"),
    ("NA", "Namibia - Republic of Namibia"),
    ("NR", "Nauru - Republic of Nauru"),
    ("NP", "Nepal - Federal Democratic Republic of Nepal"),
    ("NL", "Netherlands - Kingdom of the Netherlands"),
    ("NC", "New Caledonia"),
    ("NZ", "New Zealand"),
    ("NI", "Nicaragua - Republic of Nicaragua"),
    ("NE", "Niger - Republic of the Niger"),
    ("NG", "Nigeria - Federal Republic of Nigeria"),
    ("NU", "Niue - Niue"),
    ("NF", "Norfolk Island"),
    ("MK", "North Macedonia - Republic of North Macedonia"),
    ("MP", "Northern Mariana Islands - Commonwealth of the Northern Mariana Islands"),
    ("NO", "Norway - Kingdom of Norway"),
    ("OM", "Oman - Sultanate of Oman"),
    ("PK", "Pakistan - Islamic Republic of Pakistan"),
    ("PW", "Palau - Republic of Palau"),
    ("PS", "Palestine, State of - the State of Palestine"),
    ("PA", "Panama - Republic of Panama"),
    ("PG", "Papua New Guinea - Independent State of Papua New Guinea"),
    ("PY", "Paraguay - Republic of Paraguay"),
    ("PE", "Peru - Republic of Peru"),
    ("PH", "Philippines - Republic of the Philippines"),
    ("PN", "Pitcairn"),
    ("PL", "Poland - Republic of Poland"),
    ("PT", "Portugal - Portuguese Republic"),
    ("PR", "Puerto Rico"),
    ("QA", "Qatar - State of Qatar"),
    ("RO", "Romania"),
    ("RU", "Russian Federation"),
    ("RW", "Rwanda - Rwandese Republic"),
    ("RE", "Réunion"),
    ("BL", "Saint Barthélemy"),
    ("SH", "Saint Helena, Ascension and Tristan da Cunha"),
    ("KN", "Saint Kitts and Nevis"),
    ("LC", "Saint Lucia"),
    ("MF", "Saint Martin (French part)"),
    ("PM", "Saint Pierre and Miquelon"),
    ("VC", "Saint Vincent and the Grenadines"),
    ("WS", "Samoa - Independent State of Samoa"),
    ("SM", "San Marino - Republic of San Marino"),
    ("ST", "Sao Tome and Principe - Democratic Republic of Sao Tome and Principe"),
    ("SA", "Saudi Arabia - Kingdom of Saudi Arabia"),
    ("SN", "Senegal - Republic of Senegal"),
    ("RS", "Serbia - Republic of Serbia"),
    ("SC", "Seychelles - Republic of Seychelles"),
    ("SL", "Sierra Leone - Republic of Sierra Leone"),
    ("SG", "Singapore - Republic of Singapore"),
    ("SX", "Sint Maarten (Dutch part) - Sint Maarten (Dutch part)"),
    ("SK", "Slovakia - Slovak Republic"),
    ("SI", "Slovenia - Republic of Slovenia"),
    ("SB", "Solomon Islands"),
    ("SO", "Somalia - Federal Republic of Somalia"),
    ("ZA", "South Africa - Republic of South Africa"),
    ("GS", "South Georgia and the South Sandwich Islands"),
    ("SS", "South Sudan - Republic of South Sudan"),
    ("ES", "Spain - Kingdom of Spain"),
    ("LK", "Sri Lanka - Democratic Socialist Republic of Sri Lanka"),
    ("SD", "Sudan - Republic of the Sudan"),
    ("SR", "Suriname - Republic of Suriname"),
    ("SJ", "Svalbard and Jan Mayen"),
    ("SE", "Sweden - Kingdom of Sweden"),
    ("CH", "Switzerland - Swiss Confederation"),
    ("SY", "Syrian Arab Republic"),
    ("TW", "Taiwan, Province of China - Taiwan, Province of China"),
    ("TJ", "Tajikistan - Republic of Tajikistan"),
    ("TZ", "Tanzania, United Republic of - United Republic of Tanzania"),
    ("TH", "Thailand - Kingdom of Thailand"),
    ("TL", "Timor-Leste - Democratic Republic of Timor-Leste"),
    ("TG", "Togo - Togolese Republic"),
    ("TK", "Tokelau"),
    ("TO", "Tonga - Kingdom of Tonga"),
    ("TT", "Trinidad and Tobago - Republic of Trinidad and Tobago"),
    ("TN", "Tunisia - Republic of Tunisia"),
    ("TR", "Turkey - Republic of Turkey"),
    ("TM", "Turkmenistan"),
    ("TC", "Turks and Caicos Islands"),
    ("TV", "Tuvalu"),
    ("UG", "Uganda - Republic of Uganda"),
    ("UA", "Ukraine"),
    ("AE", "United Arab Emirates"),
    ("GB", "United Kingdom - United Kingdom of Great Britain and Northern Ireland"),
    ("US", "United States - United States of America"),
    ("UM", "United States Minor Outlying Islands"),
    ("UY", "Uruguay - Eastern Republic of Uruguay"),
    ("UZ", "Uzbekistan - Republic of Uzbekistan"),
    ("VU", "Vanuatu - Republic of Vanuatu"),
    ("VE", "Venezuela, Bolivarian Republic of - Bolivarian Republic of Venezuela"),
    ("VN", "Viet Nam - Socialist Republic of Viet Nam"),
    ("VG", "Virgin Islands, British - British Virgin Islands"),
    ("VI", "Virgin Islands, U.S. - Virgin Islands of the United States"),
    ("WF", "Wallis and Futuna"),
    ("EH", "Western Sahara"),
    ("YE", "Yemen - Republic of Yemen"),
    ("ZM", "Zambia - Republic of Zambia"),
    ("ZW", "Zimbabwe - Republic of Zimbabwe"),
    ("AX", "Åland Islands"),
]