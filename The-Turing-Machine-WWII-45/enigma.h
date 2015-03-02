/* author: James Lyons
Aug 2012
use e.g. http://practicalcryptography.com/ciphers/mechanical-era/enigma/ to generate messages
this code is from http://www.practicalcryptography.com/cryptanalysis/breaking-machine-ciphers/cryptanalysis-enigma/
*/
typedef enum rotor__{ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV,
                     ROTOR_V, ROTOR_VI, ROTOR_VII, ROTOR_VIII,
                     ROTOR_I_INV, ROTOR_II_INV, ROTOR_III_INV, ROTOR_IV_INV,
                     ROTOR_V_INV, ROTOR_VI_INV, ROTOR_VII_INV, ROTOR_VIII_INV} Rotor;

typedef enum reflector__{REFLECTOR_A, REFLECTOR_B, REFLECTOR_C} Reflector;

// a structure for storing enigma key information
typedef struct key__{
    Rotor rotors[3];
    Reflector reflector;
    int indicator[3];
    int ringsettings[3];
    char plugboard[13][2];
} EnigmaKey;    

/*******************************************************************************/                     
char reflector(Reflector r, char in);
char rotor(Rotor rotor, char in, int offset);
Rotor inverse(Rotor r);
void increment_indicator_settings(int settings[3], Rotor r[3]);
char apply_steckers(char in, char steckers[13][2]);
void enigma(EnigmaKey *key, char* ctext, char* ptext);
char enigma_encipher(char ch, EnigmaKey *key);

void initEnigmaKey(EnigmaKey *key);
void printEnigmaKey(EnigmaKey *key);
/*******************************************************************************/

