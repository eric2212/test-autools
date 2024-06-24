import requests

def dich_yaml(source_text, source_language, target_language):
  """Dịch file YAML sang ngôn ngữ khác.

  Args:
    source_text: Nội dung file YAML gốc.
    source_language: Ngôn ngữ gốc của file YAML.
    target_language: Ngôn ngữ đích để dịch.

  Returns:
    Nội dung file YAML đã được dịch.
  """

  url = "https://api.deepl.com/v2/translate"
  data = {
    "auth_key": "YOUR_DEEPL_API_KEY",
    "text": source_text,
    "source_lang": source_language,
    "target_lang": target_language
  }

  response = requests.post(url, data=data)
  if response.status_code == 200:
    return response.json()["translations"][0]["text"]
  else:
    raise Exception("Lỗi dịch: {}".format(response.text))

if __name__ == "__main__":
  # Thay thế YOUR_YAML_FILE bằng đường dẫn đến file YAML của bạn
  with open("YOUR_YAML_FILE", "r") as f:
    yaml_content = f.read()

  # Thay thế vi và en bằng ngôn ngữ gốc và ngôn ngữ đích của bạn
  translated_yaml = dich_yaml(yaml_content, "vi", "en")

  # Thay thế YOUR_TRANSLATED_YAML_FILE bằng đường dẫn đến file YAML dịch
  with open("YOUR_TRANSLATED_YAML_FILE", "w") as f:
    f.write(translated_yaml)
