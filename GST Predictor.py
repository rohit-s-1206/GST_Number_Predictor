import re

class GSTINGenerator:
    def __init__(self):
        # Dictionary of state codes and names
        self.state_codes = {
            '35': 'Andaman and Nicobar Islands',
            '37': 'Andhra Pradesh',
            '12': 'Arunachal Pradesh',
            '18': 'Assam',
            '10': 'Bihar',
            '04': 'Chandigarh',
            '22': 'Chhattisgarh',
            '26': 'Dadra and Nagar Haveli',
            '25': 'Daman and Diu',
            '07': 'Delhi',
            '30': 'Goa',
            '24': 'Gujarat',
            '06': 'Haryana',
            '02': 'Himachal Pradesh',
            '01': 'Jammu and Kashmir',
            '20': 'Jharkhand',
            '29': 'Karnataka',
            '32': 'Kerala',
            '31': 'Lakshadweep',
            '23': 'Madhya Pradesh',
            '27': 'Maharashtra',
            '14': 'Manipur',
            '17': 'Meghalaya',
            '15': 'Mizoram',
            '13': 'Nagaland',
            '21': 'Odisha',
            '34': 'Puducherry',
            '03': 'Punjab',
            '08': 'Rajasthan',
            '11': 'Sikkim',
            '33': 'Tamil Nadu',
            '36': 'Telangana',
            '16': 'Tripura',
            '09': 'Uttar Pradesh',
            '05': 'Uttarakhand',
            '19': 'West Bengal'
        }

    def validate_pan(self, pan):
        """Validate PAN number format"""
        pan_pattern = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]$')
        if not pan_pattern.match(pan):
            raise ValueError("Invalid PAN format. PAN should be in format: AAAAA9999A")
        return True

    def calculate_checksum(self, gstin_without_checksum):
        """
        Calculate checksum for GSTIN using the official algorithm
        """
        # Characters and their corresponding values
        char_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # Multiplicative factors for each position
        factors = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        
        total = 0
        for i in range(len(gstin_without_checksum)):
            curr_char = gstin_without_checksum[i]
            # Get character value from char_map
            char_val = char_map.index(curr_char)
            # Multiply with corresponding factor
            product = char_val * factors[i]
            # Add quotient and remainder of product divided by 36
            total += (product // 36) + (product % 36)
        
        # Calculate checksum
        checksum = 36 - (total % 36)
        if checksum == 36:
            checksum = 0
        
        # Convert checksum to character
        return char_map[checksum]

    def generate_gstin(self, pan, state_code, entity_number=1):
        """Generate GSTIN from PAN number"""
        try:
            # Validate inputs
            self.validate_pan(pan)
            if str(state_code).zfill(2) not in self.state_codes:
                raise ValueError("Invalid state code")
            if not (1 <= int(entity_number) <= 9):
                raise ValueError("Entity number must be between 1 and 9")

            # Format state code to 2 digits
            state_code = str(state_code).zfill(2)
            
            # Create GSTIN without checksum (14 characters)
            gstin_without_checksum = f"{state_code}{pan}{entity_number}Z"
            
            # Calculate and append checksum
            checksum = self.calculate_checksum(gstin_without_checksum)
            gstin = f"{gstin_without_checksum}{checksum}"
            
            return {
                'gstin': gstin,
                'breakdown': {
                    'state_code': f"{state_code} ({self.state_codes[state_code]})",
                    'pan': pan,
                    'entity_number': str(entity_number),
                    'z_char': 'Z',
                    'checksum': checksum
                }
            }

        except ValueError as e:
            return {'error': str(e)}

def main():
    generator = GSTINGenerator()
    
    while True:
        try:
            print("\n=== GSTIN Generator ===")
            # Get input from user
            pan = input("Enter PAN number (format AAAAA9999A): ").upper()
            
            print("\nAvailable State Codes:")
            for code, state in sorted(generator.state_codes.items()):
                print(f"{code}: {state}")
            
            state_code = input("\nEnter state code: ")
            entity_number = input("Enter entity number (1-9): ")
            
            # Generate GSTIN
            result = generator.generate_gstin(pan, state_code, entity_number)
            
            if 'error' in result:
                print(f"\nError: {result['error']}")
            else:
                print("\nGenerated GSTIN Details:")
                print(f"GSTIN: {result['gstin']}")
                print("\nBreakdown:")
                for key, value in result['breakdown'].items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
            
            # Ask if user wants to generate another GSTIN
            again = input("\nGenerate another GSTIN? (y/n): ").lower()
            if again != 'y':
                break
                
        except ValueError as e:
            print(f"\nError: {str(e)}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
