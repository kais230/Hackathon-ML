import os
import veryfi
import json

client_id = "vrfS4k6XEKzp6FWvhuvl6Hlhdflc8kBZ3P5nBhI"
client_secret = "t6MMocBzDk9WT938gZr59AJUvbPmggN4mby89aXU1DyVcvMb2ML80s7KyNKzo2ajzVzZr08wdGYyHOixCc9iLlGz1UaDwUXWDpsN7TsKy1cxo8vG1t6HB5iGOaxcPfdl"
username = "devtempmail1.tsoelzluyz"
api_key = "2c78565bdcfd6273a1160f575cc82588"

client = veryfi.Client(client_id, client_secret, username, api_key)

categories = ["Travel", "Food"]

pdf_folder = "invoices"
json_output_file = "FinalJson.json"

all_invoice_data = []

# Remove existing JSON output file if exists
if os.path.exists(json_output_file):
    os.remove(json_output_file)

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        json_result = client.process_document(pdf_path, categories)

        # Save JSON result to file
        with open(json_output_file, 'a') as json_file:
            json.dump(json_result, json_file)
            json_file.write('\n')

        # Extract required fields from json_result
        invoice_number = json_result.get('invoice_number', '')
        date = json_result.get('date', '')
        bill_to = json_result.get('bill_to', {})
        customer = bill_to.get('name', '')
        dropdown = json_result.get('line_items', [])
        item_description = dropdown[0].get('description', '') if dropdown and len(dropdown) > 0 else ''
        quantity = dropdown[0].get('quantity', '') if dropdown and len(dropdown) > 0 else ''
        price = json_result.get('total', '')
        categoriesjson = json_result.get('category', '')

        # Add the extracted data to a list
        invoice_data = {
            'Invoice Number': invoice_number,
            'Date': date,
            'Customer': customer,
            'Item Description': item_description,
            'Quantity': quantity,
            'Price': price,
            'Category': categoriesjson
        }
        all_invoice_data.append(invoice_data)

# Save the list of invoice data as a JSON file
with open(json_output_file, 'w') as json_file:
    json.dump(all_invoice_data, json_file)

print("Data saved to", json_output_file)
