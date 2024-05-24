import AAVT

# 全流程
result = AAVT.whisper_faster("video.mp4", "tiny", "cpu")
# result = AAVT.whisper_openai(result, "sk-")

result = AAVT.translate(result, "sk-", "gpt-4o")  # 默认生成output.srt文件

AAVT.merge("video.mp4", "output.srt")


# 函数说明
# result = AAVT.whisper_faster("video.mp4", "tiny", "cpu")

"""
    使用 Faster Whisper 模型进行音频转录

    -- 参数

    - **file_path**: 要识别的音频文件的路径。
    - **model**: Whisper 模型，支持 `tiny`, `tiny.en`, `base`, `base.en`, `small`, `small.en`, `medium`, `medium.en`, `large-v1`, `large-v2`, `large-v3`, `large`, `distil-small.en`, `distil-medium.en`, `distil-large-v2`, `distil-large-v3`。
    - **device**: 运行设备，可以是 `cpu` 或 `cuda`，默认值为 `cpu`。
    - **prompt**: Faster Whisper 提示词，默认值为 `None`。
    - **lang**: 指定语言，`auto` 表示自动检测语言，默认值为 `auto`。
    - **beam_size**: 束搜索宽度，影响解码过程中的候选数量，默认值为 `5`。
    - **vad**: 是否使用声音活动检测，默认值为 `False`。
    - **min_vad**: 声音活动检测的最小持续时间（毫秒），默认值为 `500`。
    - **srt**: 是否直接输出 SRT 字幕，默认值为 `False`。
    - **output_path**: SRT 字幕输出位置，如 `D://Chenyme-AAVT/output/`，默认值为 `None`。

    -- 返回值

    - **Dict**: 包含转录文本和可能的其他信息的字典，或 SRT 字幕文件。
        {
        'text': ''',
        'segments': [{
                'id': segment.id,
                'seek': segment.seek,
                'start': segment.start,
                'end': segment.end,
                'text': segment.text,
                'tokens': segment.tokens,
                'temperature': segment.temperature,
                'avg_logprob': segment.avg_logprob,
                'compression_ratio': segment.compression_ratio,
                'no_speech_prob': segment.no_speech_prob}
        }

"""

# result = AAVT.whisper_openai(result, "sk-")

"""
    使用 OpenAI API Whisper 接口进行音频转录

    -- 参数

    - **video_path**: 要识别的文件路径，如`D://Chenyme_AAVT/test.mp4`。
    - **api_key**: OpenAI API KEY。
    - **base_url**: OpenAI 代理 URL，默认值为 `https://api.openai.com/v1`。
    - **model**: Whisper 模型，默认值为 `whisper-1`。
    - **prompt**: Whisper 转录提示词，默认值为 `Don’t make each line too long.`。
    - **temperature**: 模型温度，默认值为 `0.8`。
    - **srt**: 是否直接输出 SRT 字幕，默认值为 `False`。
    - **output_path**: SRT 字幕输出位置，如 `D://Chenyme_AAVT/output/`。

    -- 返回值

    - **Dict**: 包含转录结果的字典。

"""

# result = AAVT.translate(result, "sk-", "gpt-4o")

"""
    使用翻译功能进行文本翻译
    
    -- 参数
    
    - **result**: 包含待翻译文本的字典, whisper转录后的字典。
    - **api_key**: OpenAI API KEY。
    - **base_url**: API 代理 URL，默认值为 `None`。
    - **model**: 使用的模型名称，默认值为 `None`。
        支持的平台：openai，kimi，deepseek，chatgplm，本地调用
    - **local**: 是否使用本地大模型翻译，默认值为 `False`。
    - **language**: 翻译目标语言，默认值为 `None`。
    - **wait_time**: 每次请求后的等待时间（秒），默认值为 `None`。
    - **srt**: 是否直接输出 SRT 字幕，默认值为 `False`。
    - **output_path**: SRT 字幕输出位置，如 `D://Chenyme-AAVT/output/`，默认值为 `None`。
    
    -- 返回值
    
    - **Dict**: 包含翻译结果的字典。
        {
        'text': '',
        'segments': [{
                'id': segment.id,
                'seek': segment.seek,
                'start': segment.start,
                'end': segment.end,
                'text': segment.text,
                'tokens': segment.tokens,
                'temperature': segment.temperature,
                'avg_logprob': segment.avg_logprob,
                'compression_ratio': segment.compression_ratio,
                'no_speech_prob': segment.no_speech_prob}
        }
"""

# AAVT.merge("video.mp4", "text.srt")

"""
    将视频文件与字幕文件合并,支持多种编码器预设以调整编码速度和质量。

    -- 参数

    - **video_name**: 输入视频文件的路径。
    - **srt_name**: 输入字幕文件的路径。
    - **output_path**: 输出视频文件的路径，默认值为当前目录。
    - **font**: 字幕字体名称，默认值为 'system'。
    - **font_size**: 字幕字体大小，默认值为 18。
    - **font_color**: 字幕字体颜色，默认值为 'HFFFFFF'（白色，ASS 格式）。
    - **subtitle_model**: 字幕模式，默认值为 '硬字幕'。
    - **quality**: 编码器预设，默认值为 `medium`。可选值包括：
          - `ultrafast`: 最快的编码速度，但质量最低，文件最大。
          - `superfast`: 非常快的编码速度，质量和文件大小有所提升。
          - `veryfast`: 很快的编码速度，适用于实时编码或需要快速处理的情况。
          - `faster`: 比较快的编码速度，质量进一步提高。
          - `fast`: 快速编码速度，质量较好。
          - `medium`: 默认预设，编码速度和质量的平衡点。
          - `slow`: 较慢的编码速度，输出质量更高，文件更小。
          - `slower`: 更慢的编码速度，质量进一步提高。
          - `veryslow`: 非常慢的编码速度，质量最高，文件最小。
          - `placebo`: 极慢的编码速度，质量微小提升，不推荐使用，除非对质量有极高要求且不在意编码时间。
    - **crf**: 恒定速率因子，CRF 值的范围通常为 0 到 51，数值越低，质量越高。建议值：
          - `0`: 无损压缩，质量最高，文件最大。
          - `18`: 视觉上接近无损，非常高的质量，文件较大。
          - `23`: 默认值，质量和文件大小的平衡点。
          - `28`: 较低的质量，文件较小。

    -- 返回值
    - None
"""

# str_return = AAVT.blog("video.mp4", "sk-")

"""
    将视频文件中的内容生成一篇博客文章，支持使用OpenAI的API或者本地模型进行文本转录和生成。

    -- 参数

    - **video_path**: 输入视频文件的路径，支持 `.mp4` 格式。
    - **api_key**: OpenAI API 密钥。
    - **base_url**: OpenAI API 基础URL，默认值为 `https://api.openai.com/v1`。
    - **vision**: 博客文章的视角，默认值为 `视频作者`。
    - **whisper_model**: 转录模式，支持 `api`、`faster` 和 `local`，默认值为 `api`。
    - **local_model**: 本地模型的路径，当 `whisper_model` 为 `local` 时生效。
    - **temperature**: 生成文章的温度参数，默认值为 `0.8`。
    - **output_path**: 输出文件的路径，默认值为当前工作目录。

    -- 返回值

    - **str**: 返回生成的博客文章内容。
    - **md**: Markdown格式博客。
    - **png**：博客配图。
"""