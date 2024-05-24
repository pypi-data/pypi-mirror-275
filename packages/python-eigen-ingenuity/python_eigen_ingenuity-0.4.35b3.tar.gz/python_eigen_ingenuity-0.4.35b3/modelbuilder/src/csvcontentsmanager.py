import assetmodelutilities as amu
import processors.propertymanager as pm


class CSVContentsManager:

    # Manages the contents of a .CSV file
    # Returns the data requested by the Processor classes

    def __init__(self, csv_data, header_mappings, alias_mappings, default_data_type):
        file_headers = next(csv_data)
        self.data_list = list(csv_data)
        unmapped_keys = []
        mapped_keys = []
        self.formats = []
        self.types = []

        for header in file_headers:
            this_format = ''
            this_type = ''
            split_header = header.split(':')
            this_key = split_header[0].replace('\ufeff', '')
            for format_type in split_header[1:]:
                if format_type and format_type in amu.all_types:
                    this_type += ':' + format_type
                else:
                    this_format += ':' + format_type
            if this_format == '' and default_data_type != '':
                this_format = ':' + default_data_type

            unmapped_keys += [this_key]

            # Now apply key mappings from config file
            if this_key in header_mappings:
                mapped_key = header_mappings[this_key]
            elif this_key + this_format in header_mappings:
                mapped_key = header_mappings[this_key + this_format]
            else:
                mapped_key = this_key

            if this_key in alias_mappings:
                alias_mapped_key = alias_mappings[this_key]
            else:
                alias_mapped_key = this_key

            if this_key != alias_mapped_key:
                this_mapped_key = alias_mapped_key
            elif this_key != mapped_key:
                split_mapped_key = mapped_key.split(':')
                this_mapped_key = split_mapped_key[0]
                # Mapped Key may have new format...
                if len(split_mapped_key) > 1:
                    if split_mapped_key[1] != '':
                        this_format = ':' + split_mapped_key[1]
                    else:
                        this_format = ''
            else:
                this_mapped_key = this_key
            mapped_keys += [this_mapped_key]

            self.unmapped_keys = pm.validate_properties(unmapped_keys)
            self.mapped_keys = pm.validate_properties(mapped_keys)
            self.formats += [this_format]
            self.types += [this_type]

    def get_row_count(self):
        return len(self.data_list)

    def get_column_count(self, column_name, type_list=[]):
        # Find the number of columns in the files whose heading is in the provided list
        return len(self.get_column_numbers_list(column_name, type_list))

    def get_column_numbers_list(self, column_name, type_list=[]):
        # Return a List containing the column numbers for each column in the given list of column names
        if not(isinstance(column_name, list)):
            name_list = [column_name]
        else:
            name_list = column_name
        column_list = [i for i, j in enumerate(self.mapped_keys) if (j in name_list or len(set(self.types[i].split(':')).intersection(set(type_list))) != 0)]
        return column_list

    def get_other_column_numbers_list(self, column_name, type_list=[]):
        # Return a List containing the column numbers for each column NOT in the given list of column names
        if not(isinstance(column_name, list)):
            name_list = [column_name]
        else:
            name_list = column_name
        column_list = [i for i, j in enumerate(self.mapped_keys) if not(j in name_list or len(set(self.types[i].split(':')).intersection(set(type_list))) != 0)]
        return column_list

    def get_incomplete_rows(self):
        num_headers = len(self.mapped_keys)
        incomplete_rows = []
        row_count = 0
        for a_row in self.data_list:
            row_count += 1
            if len(a_row) < num_headers:
                incomplete_rows.append(row_count)
        return incomplete_rows

    def get_column_values_list(self, row_number, column_numbers):
        # Return the values in the given row, for the columns in the provided list (skips empty values)
        # Returned as a List (of strings)
        this_row = self.data_list[row_number]
        columns_list = [this_row[i] for i in column_numbers if len(this_row[i]) > 0]
        return columns_list

    def get_column_values_list_with_formatted_keys(self, row_number, column_numbers):
        # Return the values in the given row, for the columns in the provided list (skips empty values)
        # Returned as a List (of strings)
        this_row = self.data_list[row_number]
        properties_list = [{self.mapped_keys[column]+self.formats[column]:this_row[column]} for column in column_numbers if len(this_row[column])]
        return properties_list

    def get_property_values_dict(self, row_number, column_numbers, allow_blanks=False, default_key='', prefix=''):
        this_row = self.data_list[row_number]
        split_values = [this_row[column].split('::') for column in column_numbers]
        this_list = {prefix + (self.mapped_keys[column] or default_key) + self.formats[column]: this_row[column] if len(split_values[count]) == 1 else {prefix + split_values[count][0] + self.formats[column]: split_values[count][1]} for count, column in enumerate(column_numbers) if this_row[column] or allow_blanks}
        return this_list

    def get_property_values_list(self, row_number, column_numbers, allow_blanks=False, default_key='', override_key=''):
        this_row = self.data_list[row_number]
        split_values = [this_row[column].split('::') for column in column_numbers]
        this_list = [{(override_key or self.mapped_keys[column] or default_key) + self.formats[column]: this_row[column]} if len(split_values[count]) == 1 else {split_values[count][0] + self.formats[column]: split_values[count][1]} for count, column in enumerate(column_numbers) if this_row[column] or allow_blanks]
        return this_list
