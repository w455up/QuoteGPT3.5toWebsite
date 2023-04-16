import openai
import gradio as gr

openai.api_key = "YOUR_API_KEY"

messages = [{"role": "system", "content": "填入一些機器人的背景 間接影響形成的chatbot"},
            {"role": "assistant", "content": "填入一些機器人的特色 直接影響形成的chatbot"}]

messages= []

def CustomChatGPT(user_input):
    
    messages.clear()  # 清空 messages 列表

    messages.append({"role": "user", "content": user_input})  # 將使用者輸入加入 messages 列表
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages, # 使用 OpenAI GPT-3 模型生成助理的回應
        temperature=0.8,
        max_tokens=50,
        n=1,
        stop=["quit","exit"])

#可以給你的機器人有一些預設回應--------------------------------------------------------------------------#
    question_category = ""  # 初始化問題類別為空
    if "" in user_input:  # 判斷使用者輸入中是否包含 "" 關鍵字
        question_category = ""  # 若包含則將問題類別設定為 ""
    elif "" in user_input:  # 判斷使用者輸入中是否包含 "" 關鍵字
        question_category = ""  # 若包含則將問題類別設定為 ""

    if question_category == "":  # 若問題類別為 ""
        reply = ""
    
    elif question_category == "":  # 若問題類別為 ""
        reply = ""
    
    else:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)  # 若問題類別不是 "" 或 ""，則使用 GPT-3 模型生成助理的回應
        reply = response["choices"][0]["message"]["content"]  # 取得 GPT-3 模型生成的回應內容
#----------------------------------------------------------------------------------------------------#
    messages.append({"role": "assistant", "content": reply})  # 將助理的回應加入 messages 列表
    return reply  # 回

inputs = gr.inputs.Textbox(lines=1, label="輸入:")
outputs = gr.outputs.Textbox(label="回覆:")
interface = gr.Interface(
    fn=CustomChatGPT, 
    inputs=inputs, 
    outputs=outputs, 
    title="SCU",description="在對話框輸入你想要的內容",
    theme= gr.themes.Base())

interface.launch()