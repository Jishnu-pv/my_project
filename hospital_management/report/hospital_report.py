from odoo import api, models


class PatientCard(models.AbstractModel):
    _name = 'report.hospital_management.report_patient_id_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("yes enter here")
        print("form iss", data)
        patient_card = data['form']['patient_id']
        date_from = data['form']['from_date']
        date_to = data['form']['to_date']
        dr = data['form']['doctor_id']
        department = data['form']['department_id']
        diseases = data['form']['diseases_id']
        patient_name = data['form']['patient_name_id']
        if patient_card:
            patient_cards = patient_card[1]
            patient_name = patient_name[1]
        else:
            patient_cards = False
            patient_name = False
        if dr:
            drs = dr[1]
        else:
            drs = False
        print("drrr",drs)

        if patient_card and date_from and date_to and dr and department and diseases:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
            he.name as doctor,ht.date as date,
            hemp.name as department,hd.disease as diseases 
            from hospital_ticket ht
            INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
            INNER JOIN res_partner rs ON rs.id = hp.patient_id
            INNER JOIN hr_employee he ON ht.doctor_id = he.id
            INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
            INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
            INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id
               
            WHERE hd.disease = '""" + str(diseases[1]) + """' 
            AND hemp.name = '""" + str(department[1]) + """' AND 
            hp.name = '""" + str(patient_card[1]) + """'  AND  
            ht.date BETWEEN '""" + str(
                date_from) + """"' AND '""" + str(date_to) + """"'
                 and he.name = '""" + str(dr[1]) + """'
                             
                """
        elif patient_card and date_from and date_to :
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                        he.name as doctor,ht.date as date,
                        hemp.name as department,hd.disease as diseases 
                        from hospital_ticket ht
                        INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                        INNER JOIN res_partner rs ON rs.id = hp.patient_id
                        INNER JOIN hr_employee he ON ht.doctor_id = he.id
                        INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                        INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                        INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id
               
                WHERE hp.name = '""" + str(patient_card[1]) + """' and   ht.date BETWEEN '""" + str(
                date_from) + """"' AND '""" + str(date_to) + """"' 
                             
                """

        elif date_from and date_to:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                he.name as doctor,ht.date as date,
                hemp.name as department,hd.disease as diseases 
                from hospital_ticket ht
                INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                 INNER JOIN res_partner rs ON rs.id = hp.patient_id
                INNER JOIN hr_employee he ON ht.doctor_id = he.id
                INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                  INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                 INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id
                             
                WHERE  ht.create_date BETWEEN '""" + str(
                date_from) + """"' AND '""" + str(date_to) + """"' 
                             
                             """

        elif patient_card:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                  he.name as doctor,ht.date as date,
                  hemp.name as department,hd.disease as diseases 
                 from hospital_ticket ht
                 INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                INNER JOIN res_partner rs ON rs.id = hp.patient_id
                INNER JOIN hr_employee he ON ht.doctor_id = he.id
                 INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id

                WHERE hp.name = '""" + str(patient_card[1]) + """' """
        elif diseases:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                  he.name as doctor,ht.date as date,
                hemp.name as department,hd.disease as diseases 
                 from hospital_ticket ht
                INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                 INNER JOIN res_partner rs ON rs.id = hp.patient_id
                INNER JOIN hr_employee he ON ht.doctor_id = he.id
                INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                 INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id

             WHERE   hd.diseases_id = '""" + str(diseases[1]) + """' """

        elif patient_card and dr and diseases:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                he.name as doctor,ht.date as date,
                hemp.name as department,hd.disease as diseases 
                 from hospital_ticket ht
                INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                 INNER JOIN res_partner rs ON rs.id = hp.patient_id
                 INNER JOIN hr_employee he ON ht.doctor_id = he.id
                  INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id
                       WHERE   hd.diseases_id = '""" + str(
                    diseases) + """' and hp.name = '""" + str(
                patient_card[1]) + """' and he.name = '""" + str(dr[1]) + """'
                    """
        elif dr:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                 he.name as doctor,ht.date as date,
                hemp.name as department,hd.disease as diseases 
                from hospital_ticket ht
                INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                INNER JOIN res_partner rs ON rs.id = hp.patient_id
                INNER JOIN hr_employee he ON ht.doctor_id = he.id
                INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id

                     WHERE   he.name = '""" + str(dr[1]) + """'
                                   """

        if date_from:
            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
            he.name as doctor,ht.date as date,
            hemp.name as department,hd.disease as diseases 
            from hospital_ticket ht
            INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
            INNER JOIN res_partner rs ON rs.id = hp.patient_id
            INNER JOIN hr_employee he ON ht.doctor_id = he.id
            INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
            INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
            INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id
             WHERE  ht.create_date >= '""" + str(
            date_from) + """"'
            """



        else:

            q = """select hp.name as sl,ht.tocken_no as tocken_no,rs.name,
                he.name as doctor,ht.date as date,hemp.name as department,
                hd.disease as diseases  from 
                hospital_ticket ht 
                INNER JOIN hospital_patient hp ON ht.patient_id = hp.id
                INNER JOIN res_partner rs  ON rs.id = hp.patient_id
                INNER JOIN hr_employee he  ON ht.doctor_id = he.id
                INNER JOIN hr_department hemp  ON ht.department_id = hemp.id
                INNER JOIN hospital_consultation hc  ON ht.patient_id = hc.id
                INNER JOIN hospital_disease hd  ON hd.id = hc.disease_id
                
                """

        self.env.cr.execute(q)
        # temp = self.env.cr.fetchall()
        # docs = temp['field']
        docs = self.env.cr.dictfetchall()
        # print("kkkk>>>", docs[0])
        # print("here docss", q)
        print("here docss", docs)
        return {
            'doc_ids': docids,
            'doc_model': 'hospital.patient',
            'docs': docs,
            'data': data,
            'date_from':date_from,
            'date_to':date_to,
            'patient_card':patient_cards,
            'patient_name':patient_name,
            'doctor':drs


        }
