def caesar_encrypt(plaintext: str, keyword: str) -> str:
    """
    Encrypt the plaintext using the advanced Caesar cipher with a keyword.

    Args:
    plaintext (str): The text to be encrypted.
    keyword (str): The keyword used for determining the shift.

    Returns:
    str: The encrypted text.

    Example:
    >>> caesar_encrypt("HELLO WORLD", "KEY")
    "RIJVS UYVJN"
    """
    ans = ""
    CONST_ORD1 = ord('A')
    CONST_ORD2 = ord('a')
    keyword_pos = 0
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                shift = ord(keyword[keyword_pos].upper()) - CONST_ORD1
                ans += chr((ord(plaintext[i]) + shift - CONST_ORD1) % 26 + CONST_ORD1)
                keyword_pos = (keyword_pos + 1) % len(keyword)
            else:
                shift = ord(keyword[keyword_pos].lower()) - CONST_ORD2
                ans += chr((ord(plaintext[i]) + shift - CONST_ORD2) % 26 + CONST_ORD2)
                keyword_pos = (keyword_pos + 1) % len(keyword)
        else:
            ans += plaintext[i]
    return ans

def caesar_decrypt(ciphertext: str, keyword: str) -> str:
    """
    Decrypt the ciphertext using the advanced Caesar cipher with a keyword.

    Args:
    ciphertext (str): The text to be decrypted.
    keyword (str): The keyword used for determining the shift.

    Returns:
    str: The decrypted text.

    Example:
    >>> caesar_decrypt("RIJVS UYVJN", "KEY")
    "HELLO WORLD"
    """
    ans = ""
    CONST_ORD1 = ord('A')
    CONST_ORD2 = ord('a')
    keyword_pos = 0
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                shift = ord(keyword[keyword_pos].upper()) - CONST_ORD1
                ans += chr((ord(ciphertext[i]) - shift - CONST_ORD1 + 26) % 26 + CONST_ORD1)
                keyword_pos = (keyword_pos + 1) % len(keyword)
            else:
                shift = ord(keyword[keyword_pos].lower()) - CONST_ORD2
                ans += chr((ord(ciphertext[i]) - shift - CONST_ORD2 + 26) % 26 + CONST_ORD2)
                keyword_pos = (keyword_pos + 1) % len(keyword)
        else:
            ans += ciphertext[i]
    return ans

print(caesar_decrypt("RIJVS UYVJN", "KEY"))