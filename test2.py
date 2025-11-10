import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForCausalLM

MODEL_NAME = "distilgpt2"  # компактная модель с TF-поддержкой

print("Загружаю модель...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = TFAutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Если у токенизатора нет pad_token — создаем
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    model.resize_token_embeddings(len(tokenizer))

# История диалога
chat_history_ids = None

def generate_reply(user_text: str,
                   max_new_tokens: int = 80,
                   temperature: float = 0.8,
                   top_p: float = 0.9,
                   top_k: int = 50) -> str:
    global chat_history_ids

    # Текст пользователя + разделитель
    new_input_ids = tokenizer.encode(
        f"User: {user_text}\nBot:",
        return_tensors="tf"
    )

    # Приклеиваем к истории
    if chat_history_ids is not None:
        input_ids = tf.concat([chat_history_ids, new_input_ids], axis=-1)
    else:
        input_ids = new_input_ids

    # Генерация ответа
    output_ids = model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        pad_token_id=tokenizer.pad_token_id,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        eos_token_id=tokenizer.eos_token_id
    )

    # Обновляем историю
    chat_history_ids = output_ids

    # Достаём только продолжение после последнего ввода
    generated_ids = output_ids[0][input_ids.shape[-1]:]
    bot_text = tokenizer.decode(generated_ids, skip_special_tokens=True)

    # Немного подчистим
    bot_text = bot_text.strip()

    # Часто модель продолжает "User:" — обрежем по этому маркеру, если появится
    stop_tokens = ["User:", "\nUser", "\nHuman:"]
    for stop in stop_tokens:
        idx = bot_text.find(stop)
        if idx != -1:
            bot_text = bot_text[:idx].strip()
            break

    return bot_text if bot_text else "Не совсем понял, переформулируй, пожалуйста 🙂"

def main():
    print("Чат-бот на TensorFlow запущен.")
    print("Напиши что-нибудь. /exit для выхода.")
    print("-" * 40)

    while True:
        user_text = input("Пользователь: ").strip()
        if user_text.lower() in ("/exit", "exit", "quit", "выход"):
            print("Бот: Было приятно пообщаться! Пока 👋")
            break
        if not user_text:
            continue

        bot_reply = generate_reply(user_text)
        print(f"Бот: {bot_reply}")
        print("-" * 40)

if __name__ == "__main__":
    main()
