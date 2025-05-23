# 🔐 CipherNest 🔐

#### BSCS 3A

#### May 2025

---

## 👥 Members:
1. Jayp Bazar *(Leader / Programmer)*
2. Mark Wayne Cleofe *(Programmer)*
3. Quennie Magno *(Designer / Documentation)*

---

## 📘 Introduction

CipherNest is an educational platform designed to simplify the exploration of cryptographic algorithms. The project provides users with an interactive environment to experiment with encryption, decryption, and hashing techniques. Its primary goal is to offer hands-on learning and demystify complex cryptographic concepts.

In the digital era, cryptography is the backbone of secure communication, data protection, and privacy. It is essential for safeguarding sensitive information against threats. CipherNest bridges the gap between theory and practical application, allowing users to understand and appreciate the critical role cryptography plays in technology and security.

---

## 🎯 Project Objectives

1. To provide an interactive platform for users to learn about cryptographic algorithms.
2. To implement and demonstrate both symmetric and asymmetric encryption techniques.
3. To showcase hashing algorithms and illustrate their differences and use cases.
4. To emphasize the importance of cryptography in secure communications and data protection.
---

## 🧠 Discussions
### Application Architecture
The CipherNest application is structured as a web-based platform that combines a responsive frontend with a robust backend to support cryptographic algorithm demonstrations. Here's an overview of its architecture:

**1. Frontend:** 

- The user interface is built using **HTML**, **CSS**, and **Bootstrap**, ensuring a responsive and visually appealing design.
- Navigation between different cryptographic algorithms is facilitated via a well-organized sidebar and buttons.
- Custom templates allow dynamic content rendering using Flask.
  
**2. Backend:** 

- The backend is developed in **Python**, leveraging the **Flask** framework for routing and server-side logic.
- Cryptographic operations are implemented using Python libraries like hashlib, pycryptodome, and custom logic for simpler algorithms.

**3. Routing:**

- Organized through Flask templates to navigate between different cryptographic algorithm demonstrations.

**4. Integration:**

- Inputs from the user are processed through forms, and the backend performs the cryptographic operations. The results are then displayed dynamically on the same page.

### Cryptographic Algorithms

**Caesar Cipher (Symmetric Encryption)**

- **History/Background:** One of the simplest and oldest encryption techniques, attributed to Julius Caesar, who used it to encode military messages.
- **How it Works:** Each letter in the plaintext is shifted by a fixed number of positions in the alphabet.
    -  **Pseudocode:**
            <!-- ( Screenshots of a Pseudocode )  -->
- **Libraries Used:** Pure Python implementation (no external libraries).
- **Integration:** Users enter plaintext and a shift value. The backend computes the ciphertext and returns it to the frontend.

**Block Cipher (Symmetric Encryption)**

- **History/Background:** A more modern approach to encryption, block ciphers process data in fixed-size blocks (e.g., 64 or 128 bits) using a secret key.
- **How it Works:** Data is divided into blocks, and each block is encrypted independently using a key.
    -  **Pseudocode:**
               <!-- ( Screenshots of a Pseudocode )  -->
- **Libraries Used:** pycryptodome for block cipher implementation.
- **Integration:** Users input text, and the algorithm encrypts it block by block, displaying the resulting ciphertext.

**RSA (Asymmetric Encryption)**


---

## 🧪 Sample Run / Outputs

<!-- Include screen snippets (screenshots) or text-based output examples for each algorithm's functionality (encryption, decryption, hashing for both text and files where applicable). Embed images directly in the README.md or link to them within the repository. Use Markdown code blocks for text output. -->
