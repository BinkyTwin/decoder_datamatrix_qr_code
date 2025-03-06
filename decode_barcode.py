import cv2
import os
import numpy as np
from pyzbar.pyzbar import decode
from pylibdmtx.pylibdmtx import decode as decode_datamatrix

def decode_barcode(image_path):
    # Vérifier si l'image peut être chargée
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        return "Erreur : Impossible de charger l'image. Vérifiez le chemin et le format."
    
    # Essayer de décoder comme un QR Code avec pyzbar
    qr_codes = decode(image)
    qr_results = [qr.data.decode('utf-8') for qr in qr_codes] if qr_codes else []
    
    # Essayer de décoder comme un Data Matrix avec pylibdmtx
    datamatrix_codes = decode_datamatrix(image)
    dm_results = [dm.data.decode('utf-8') for dm in datamatrix_codes] if datamatrix_codes else []
    
    # Fusionner les résultats des deux types de codes
    all_results = qr_results + dm_results
    
    return all_results if all_results else "Aucun code lisible trouvé."

# Définir un chemin d'image universel (relatif au script)
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "image.jpeg")

decoded_texts = decode_barcode(image_path)

if isinstance(decoded_texts, list) and decoded_texts:
    print("✅ Codes détectés :")
    for text in decoded_texts:
        print(f"- {text}")
else:
    print("❌", decoded_texts)
