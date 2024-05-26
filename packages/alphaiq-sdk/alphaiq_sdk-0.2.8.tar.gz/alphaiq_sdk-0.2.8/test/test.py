import example_functions as aiq
import csv
import uuid
from datetime import date

def to_csv(output_checks):
    today_date = date.today()
    random_string = str(uuid.uuid4().hex)[:8]  # You can adjust the length as needed
    filename = f'output_checks_{today_date}_{random_string}.csv'
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['function','output', 'outcome']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for check in output_checks:
            writer.writerow(check)

function_list = [
    aiq.get_quant_linguistics_signals(),
    aiq.get_bulk_signals_all(),
    aiq.get_bulk_signals_top_level(),
    aiq.get_models_corporate_transparency(),
    aiq.get_bulk_model(),
    aiq.get_company_identifiers_map_compositeFigi(),
    aiq.get_company_identifiers_map_cik(),
    aiq.get_company_identifiers_map_consilienceId(),
    aiq.get_company_identifiers_map_cusip(),
    aiq.get_company_identifiers_map_figi(),
    aiq.get_company_identifiers_map_isin(),
    aiq.get_company_identifiers_map_lei(),
    aiq.get_company_identifiers_map_shareClassFigi(),
    aiq.get_company_identifiers_map_ticker(),
    aiq.get_bulk_mapping(),
    aiq.get_signal_explanations(),
    aiq.get_question_answer(),
    aiq.get_trending_content(),
    aiq.get_compass_report_pdf()
]

output_checks= []
i=0
for function in function_list:
    i+=1
    print(f'Trying function --> {i}')
    if "message" in function[0]:
        outcome = 'Fail'
    elif "data" in function[0]:
        outcome = 'Pass'
    elif "errors" in function[0]:
        outcome = 'Fail'
    output_checks.append({'function':function[1],'output':function[0], 'outcome': outcome})

# print(f'Result of tests: {output_checks}')

to_csv(output_checks)