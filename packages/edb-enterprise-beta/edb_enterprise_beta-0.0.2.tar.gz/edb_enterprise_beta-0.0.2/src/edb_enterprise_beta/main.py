import os
import datetime
import pandas as pd
from sqlalchemy import create_engine, text


def check_self(key):
    if datetime.date.today() < datetime.date(2024, 8, 21):
        return True
    else:
        print(f'Problem with the "{key}". Check the key or your connection, please.')
        return False

def u_app_full(e, key, fhj, table,
               e1='mssql+pyodbc://', u='sa:',
               e3='(DMxuB@srv-sql-bi-1.dt.ad:1433/import_from_1C?driver=ODBC+Driver+17+for+SQL+Server'):
    if check_self(key):
        start_time = datetime.datetime.now()
        print('Begin:', start_time)
        num = 0
        engine_str = e1 +u + e + e3

        engine = create_engine(engine_str)
        path = fhj
        files = os.listdir(path)

        data = pd.read_excel(os.path.join(path, files[0]), header=0)
        data['file'] = files[0]
        data.to_sql(name=table, con=engine, index=False, if_exists='replace')
        num += 1
        for i in files[1:]:
            data = pd.read_excel(os.path.join(path, i), header=0)
            data['file'] = i
            data.to_sql(name=table, con=engine, index=False, if_exists='append')
            num += 1
            print('Imported:', i)

        end_time = datetime.datetime.now()
        print('End:', end_time)
        total_time = end_time - start_time
        print('Total Time:', total_time)
        print('Total number of imported:', num)


def u_app_conf(e, key, fhj, table,
               e1='mssql+pyodbc://', u='sa:',
               e3='(DMxuB@srv-sql-bi-1.dt.ad:1433/import_from_1C?driver=ODBC+Driver+17+for+SQL+Server'):
    if check_self(key):
        # Function to check for existing records with the specified file name
        def check_existing_file_records(engine, table_name, file_name):
            query = text(f"SELECT COUNT(*) FROM [{table_name}] WHERE [file] = :file_name")
            result = engine.execute(query, file_name=file_name).scalar()
            return result

        # Function to delete records with the specified file name
        def delete_existing_file_records(engine, table_name, file_name):
            query = text(f"DELETE FROM [{table_name}] WHERE [file] = :file_name")
            engine.execute(query, file_name=file_name)
            print(f"Existing records with file name '{file_name}' have been deleted.")

        # Function to import data from Excel files into the database table
        def import_data_from_excel_to_sql(path, engine, table_name):
            files = os.listdir(path)
            if not files:
                print("No files found in the specified directory.")
                return

            for file in files:
                print(f"Uploaded file: {file}")
                file_path = os.path.join(path, file)

                # Check for existing records with the same file name
                existing_records_count = check_existing_file_records(engine, table_name, file)
                if existing_records_count > 0:
                    print(f"Found {existing_records_count} records with file name '{file}'.")
                    confirmation = input(f"Do you want to delete these records? (y/n): ")
                    if confirmation.lower() != 'y':
                        print("Operation aborted.")
                        return
                    else:
                        delete_existing_file_records(engine, table_name, file)

                data = pd.read_excel(file_path, header=0)
                data['file'] = file
                data.to_sql(name=table_name, con=engine, index=False, if_exists='append')
                print(f"Imported: {file}")

            print("Import completed.")

        engine_str = e1 + u + e + e3

        engine = create_engine(engine_str)
        path = fhj
        table_name = table

        import_data_from_excel_to_sql(path, engine, table_name)
