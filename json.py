import Evtx.Evtx as evtx
import xmltodict
import json
import os

def convert_evtx_to_json(evtx_path, output_path):
    try:
        with evtx.Evtx(evtx_path) as log:
            events = []
            for record in log.records():
                try:
                    xml = record.xml()
                    event_dict = xmltodict.parse(xml)
                    events.append(event_dict)
                except Exception as e:
                    print(f"Error parsing record: {e}")
            with open(output_path, 'w', encoding='utf-8') as out_file:
                json.dump(events, out_file, indent=2)
            print(f"\n✅ Conversion complete! Output saved to: {output_path}")
    except FileNotFoundError:
        print("❌ The specified .evtx file does not exist.")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("==== Windows Event Log (.evtx) to JSON Converter ====\n")
    evtx_path = input("Enter full path to .evtx file: ").strip().strip('"')

    if not evtx_path.lower().endswith('.evtx'):
        print("❌ Error: Not a valid .evtx file.")
        return

    if not os.path.isfile(evtx_path):
        print("❌ File does not exist. Please check the path.")
        return

    base_name = os.path.basename(evtx_path).replace('.evtx', '')
    output_path = os.path.join(os.path.dirname(evtx_path), f"{base_name}_converted.json")

    convert_evtx_to_json(evtx_path, output_path)

if __name__ == "__main__":
    main()
