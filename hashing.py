import hashlib

class MD5Hash:
    """
    Implementation of MD5 hashing algorithm.
    """
    
    @staticmethod
    def generate_hash(text: str) -> str:
        """
        Generates MD5 hash of input text.
        
        Args:
            text: The input text to hash
            
        Returns:
            A string containing the hexadecimal MD5 hash
        """
        try:
            # Convert input to bytes and generate hash
            message = text.encode('utf-8')
            md5_hash = hashlib.md5()
            md5_hash.update(message)
            return md5_hash.hexdigest()
        except Exception as e:
            return f"Error generating hash: {str(e)}"
    
    @staticmethod
    def verify_hash(text: str, hash_to_verify: str) -> bool:
        """
        Verifies if input text matches a given MD5 hash.
        
        Args:
            text: The input text to check
            hash_to_verify: The MD5 hash to verify against
            
        Returns:
            Boolean indicating if the hashes match
        """
        try:
            generated_hash = MD5Hash.generate_hash(text)
            return generated_hash.lower() == hash_to_verify.lower()
        except Exception:
            return False
        
    @staticmethod
    def generate_file_hash(file_path: str) -> str:
        """
        Generates MD5 hash of a text file.
        
        Args:
            file_path: Path to the text file to hash
            
        Returns:
            A string containing the hexadecimal MD5 hash of the file contents
        """
        try:
            md5_hash = hashlib.md5()
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the text file line by line
                for line in file:
                    md5_hash.update(line.encode('utf-8'))
            return md5_hash.hexdigest()
        except Exception as e:
            return f"Error generating file hash: {str(e)}"

    @staticmethod
    def verify_file_hash(file_path: str, hash_to_verify: str) -> bool:
        """
        Verifies if a file matches a given MD5 hash.
        
        Args:
            file_path: Path to the file to check
            hash_to_verify: The MD5 hash to verify against
            
        Returns:
            Boolean indicating if the file hash matches
        """
        try:
            generated_hash = MD5Hash.generate_file_hash(file_path)
            return generated_hash.lower() == hash_to_verify.lower()
        except Exception:
            return False
        
class SHA1Hash:
    """
    Implementation of SHA-1 hashing algorithm.
    """
    
    @staticmethod
    def generate_hash(text: str) -> str:
        """
        Generates SHA-1 hash of input text.
        
        Args:
            text: The input text to hash
            
        Returns:
            A string containing the hexadecimal SHA-1 hash
        """
        try:
            # Convert input to bytes and generate hash
            message = text.encode('utf-8')
            sha1_hash = hashlib.sha1()
            sha1_hash.update(message)
            return sha1_hash.hexdigest()
        except Exception as e:
            return f"Error generating hash: {str(e)}"
    
    @staticmethod
    def verify_hash(text: str, hash_to_verify: str) -> bool:
        """
        Verifies if input text matches a given SHA-1 hash.
        
        Args:
            text: The input text to check
            hash_to_verify: The SHA-1 hash to verify against
            
        Returns:
            Boolean indicating if the hashes match
        """
        try:
            generated_hash = SHA1Hash.generate_hash(text)
            return generated_hash.lower() == hash_to_verify.lower()
        except Exception:
            return False
        
class SHA256Hash:
    """
    Implementation of SHA-256 hashing algorithm.
    """
    
    @staticmethod
    def generate_hash(text: str) -> str:
        """
        Generates SHA-256 hash of input text.
        
        Args:
            text: The input text to hash
            
        Returns:
            A string containing the hexadecimal SHA-256 hash
        """
        try:
            # Convert input to bytes and generate hash
            message = text.encode('utf-8')
            sha256_hash = hashlib.sha256()
            sha256_hash.update(message)
            return sha256_hash.hexdigest()
        except Exception as e:
            return f"Error generating hash: {str(e)}"
    
    @staticmethod
    def verify_hash(text: str, hash_to_verify: str) -> bool:
        """
        Verifies if input text matches a given SHA-256 hash.
        
        Args:
            text: The input text to check
            hash_to_verify: The SHA-256 hash to verify against
            
        Returns:
            Boolean indicating if the hashes match
        """
        try:
            generated_hash = SHA256Hash.generate_hash(text)
            return generated_hash.lower() == hash_to_verify.lower()
        except Exception:
            return False
        
class SHA512Hash:
    """
    Implementation of SHA-512 hashing algorithm.
    """
    
    @staticmethod
    def generate_hash(text: str) -> str:
        """
        Generates SHA-512 hash of input text.
        
        Args:
            text: The input text to hash
            
        Returns:
            A string containing the hexadecimal SHA-512 hash
        """
        try:
            # Convert input to bytes and generate hash
            message = text.encode('utf-8')
            sha512_hash = hashlib.sha512()
            sha512_hash.update(message)
            return sha512_hash.hexdigest()
        except Exception as e:
            return f"Error generating hash: {str(e)}"
    
    @staticmethod
    def verify_hash(text: str, hash_to_verify: str) -> bool:
        """
        Verifies if input text matches a given SHA-512 hash.
        
        Args:
            text: The input text to check
            hash_to_verify: The SHA-512 hash to verify against
            
        Returns:
            Boolean indicating if the hashes match
        """
        try:
            generated_hash = SHA512Hash.generate_hash(text)
            return generated_hash.lower() == hash_to_verify.lower()
        except Exception:
            return False