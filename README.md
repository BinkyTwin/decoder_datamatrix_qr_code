# Decode Barcode (QR Code & Data Matrix)

## 📌 Description
Ce script permet de lire et de décrypter des codes **QR** et **Data Matrix** à partir d'une image. Il utilise les bibliothèques OpenCV, Pyzbar et Pylibdmtx pour analyser l'image et extraire les informations des codes détectés.

## 🛠️ Prérequis
Avant d'exécuter le script, assurez-vous d'avoir Python installé sur votre machine (version 3.7 ou supérieure). Vous devez également installer les dépendances nécessaires.

### 📦 Installation des dépendances
Exécutez la commande suivante pour installer les bibliothèques requises :
```bash
pip install opencv-python numpy pyzbar pylibdmtx
```

Sous Linux, certaines bibliothèques système sont requises. Installez-les avec :
```bash
sudo apt update
sudo apt install libzbar0 libdmtx0t64
```

## 🚀 Utilisation
1. **Ajoutez une image contenant un QR Code ou un Data Matrix** dans le même dossier que le script et renommez-la `image.jpeg`.
2. **Exécutez le script** avec la commande :
   ```bash
   python decode_barcode.py
   ```
3. **Résultat** :
   - Si un ou plusieurs codes sont détectés, leur contenu sera affiché.
   - Si aucun code n'est trouvé ou si l'image est invalide, un message d'erreur sera affiché.

## 📂 Structure du projet
```
📁 Projet
│── decode_barcode.py  # Script principal
│── image.jpeg         # Image à scanner
│── README.md          # Documentation
```

## 📝 Remarques
- Le script fonctionne avec **les QR Codes et les Data Matrix**.
- Assurez-vous que l’image est de **bonne qualité** pour éviter les erreurs de lecture.
- Vous pouvez modifier `image.jpeg` dans le script pour analyser d'autres fichiers.

## 🤝 Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, n'hésitez pas à proposer des modifications via un **pull request** sur GitHub.

## 📜 Licence
Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier selon vos besoins.

