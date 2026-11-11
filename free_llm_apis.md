# Бесплатные тарифы LLM API: что подтверждено официальными страницами

Дата проверки: 12 ноября 2026. Данные собраны двумя способами: чтением официальных страниц (через веб-загрузку) и ручной проверкой пользователя там, где страницы не отдали нужное. В столбце «Проверка» указано, какой способ использован для каждой строки. Если факта нет на официальной странице, так и написано («не указано на странице»). Цифры не взяты из памяти и не округлены.

## Сводная таблица

| Сервис | Бесплатные модели или стартовые кредиты | Лимиты | Нужна карта? | Официальные страницы | Проверка (12.11.2026) |
|---|---|---|---|---|---|
| **Anthropic (Claude API)** | Постоянного бесплатного тарифа нет. Стартовых кредитов нет, баланс нового аккаунта $0 | Лимиты платных уровней, см. раздел ниже | Не указано на странице. Принимаются банковские карты | [цены](https://platform.claude.com/docs/en/about-claude/pricing), [лимиты](https://platform.claude.com/docs/en/api/rate-limits) | Вручную (аккаунт пользователя) и чтение страниц |
| **Vercel AI Gateway** | $5 кредитов в месяц на каждый team account, только для моделей из списка Free Tier eligible | Ниже, чем на платном тарифе; числа не опубликованы | Требование карты не подтверждено однозначно | [цены](https://vercel.com/docs/ai-gateway/pricing), [лимиты](https://vercel.com/docs/ai-gateway/rate-limits), [старт](https://vercel.com/docs/ai-gateway/getting-started) | Вручную по странице цен (last updated 8 сентября 2026) |
| **Google AI Studio (Gemini API)** | Бесплатный тариф («Free of charge») у ряда моделей, например Gemini 3.8 Flash, 3.6 Flash, 3.5 Flash-Lite | На странице не напечатаны, смотреть в AI Studio. Квоты на проект, сброс в полночь по тихоокеанскому времени | Не указано на странице | [цены](https://aistudio.google.com/docs/pricing), [лимиты](https://aistudio.google.com/docs/rate-limits) | Чтение страниц; часть списка моделей из пересказа |
| **OpenRouter (`:free`)** | Модели с суффиксом `:free`, список меняется | 20 запросов в минуту; 50 в день при покупке менее 10 кредитов, 1000 в день при покупке не менее 10 | Не указано на странице | [лимиты](https://openrouter.ai/docs/api-reference/limits), [FAQ](https://openrouter.ai/docs/faq), [цены](https://openrouter.ai/pricing) | Чтение страниц |
| **Groq** | План Free: gpt-oss-120b, gpt-oss-20b, qwen3.8-27b, allam-2-7b, whisper-large-v3, orpheus-v1-english | Базовые лимиты Free (на Developer выше), таблица в разделе ниже | Для Free не указано; для апгрейда на Developer нужен способ оплаты | [лимиты](https://console.groq.com/docs/rate-limits), [биллинг](https://console.groq.com/docs/billing-faqs), [Organization Limits](https://console.groq.com/settings/limits) (нужен вход) | Вручную по странице Organization Limits |
| **DeepSeek** | Бесплатного тарифа на прочитанных страницах нет | Нет RPM/TPM; лимит одновременных запросов на аккаунт: 2500 (deepseek-flash), 500 (deepseek-v4-pro) | Не указано на странице | [цены](https://api-docs.deepseek.com/quick_start/pricing/), [лимиты](https://api-docs.deepseek.com/quick_start/rate_limit) | Чтение страниц; FAQ и платформа недоступны |
| **Kimi (Moonshot)** | Бесплатного тарифа нет. Минимальное пополнение $1, после накопленных $5 дают ваучер $5 | Зависят от суммы пополнений; таблица на странице пустая | Не указано; для частных лиц названы WeChat Pay и Alipay | [лимиты](https://platform.kimi.ai/docs/pricing/limits), [цены](https://platform.kimi.ai/docs/pricing/chat), [оплата](https://platform.kimi.ai/docs/guide/account-and-payments) | Чтение страниц; числа лимитов не получены |

## Подробно по сервисам

### Anthropic (Claude API)

- **Бесплатный тариф.** Постоянного бесплатного тарифа нет, API оплачивается по факту использования.
- **Стартовые кредиты.** Стартовых кредитов нет, баланс нового аккаунта $0. Это подтверждено ручной проверкой (аккаунт пользователя). Страница цен в пересказе содержала фразу про «небольшие бесплатные кредиты для тестирования API» без суммы; ручная проверка её не подтвердила, поэтому на неё рассчитывать нельзя.
- **Кредиты по подписке.** Планы Max, Ultra и Team включают ежемесячные API-кредиты; планы Free, Pro и Enterprise под них не подходят ([страница](https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers), [справка](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)). Это не бесплатный API-тариф: нужна платная подписка.
- **Лимиты платных уровней.** Уровни Start, Build, Scale, Custom. «Новые организации … могут начать с уровня Evaluation, лимиты ниже стандартных». Цифры Evaluation на странице не указаны. Для уровня Start (запросы / входные токены / выходные токены в минуту): Claude Opus 5.5, Sonnet 5.5, Haiku 5.5 — 4 000 / 2 000 000 / 400 000; Claude Opus 5, Sonnet 5, Haiku 4.5 — 1 000 / 2 000 000 / 400 000; Claude Fable 5.x — 4 000 / 500 000 / 100 000. Месячный лимит расходов уровня Start — 500 долларов США.
- **Карта.** Требования при регистрации на странице не указаны. Сумма предоплаты для первого уровня на странице не указана.
- **Исследовательские программы** (по результатам поиска, страницы целиком не читались): External Researcher Access Program — $1000 кредитов для исследователей безопасности, AI for Science Program — до $20 000 на 6 месяцев.

### Vercel AI Gateway

Источник: [vercel.com/docs/ai-gateway/pricing](https://vercel.com/docs/ai-gateway/pricing) (last updated 8 сентября 2026), проверено вручную 12 ноября 2026.

- **Бесплатный тариф.** $5 кредитов в месяц, включены в каждый Vercel team account.
- **Только для части моделей.** $5 действуют только на модели из списка Free Tier eligible, а не на весь каталог. В каталоге на странице моделей видны модели с тегом `free`, например `nvidia/nemotron-3.5-lightning-free`, `humansand/ampersand-v0.1`, `stealth/glyph-cluster`; это неполный список, часть каталога не читалась.
- **Лимиты.** Rate limits ниже, чем на платном тарифе. Числа не опубликованы: «Limits can change, so this page describes behavior rather than fixed numbers»; превышение даёт HTTP 429.
- **BYOK** (свои ключи провайдеров) на free tier недоступен: нужен платный тариф и купленные кредиты.
- **Начало отсчёта.** Кредиты начинают действовать с первого запроса.
- **Переход на платный.** При покупке кредитов аккаунт переходит на paid tier, ежемесячный бесплатный кредит больше не начисляется.
- **Карта: требование не подтверждено однозначно.** В тексте страницы цен для free tier карта не требуется, но на странице Getting started сказано: «To use free AI Gateway Credits, add a valid payment method to your team».
- **Нерешённый вопрос.** В сообществе Vercel есть сообщения, что бесплатный кредит перестал обновляться, а Vercel Agent назвал его одноразовым грантом. Официального ответа я не нашёл; это противоречит странице цен, поэтому проверяйте баланс в дашборде.

### Google AI Studio (Gemini API)

- Страницы `ai.google.dev/gemini-api/docs/*` перенаправляют (301) на `aistudio.google.com/docs/*`, ссылки в таблице уже на новые адреса.
- **Бесплатные модели (дословно со страницы цен):** Gemini 3.8 Flash (`gemini-3.8-flash`), Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, а также Gemini 3.5 Transcribe и несколько Live-моделей. Модели Gemini 4 Carbon и Gemini 4 Argon на Free «not available». Дополнительный список (Gemini 3.1 Flash-Lite, Gemini 2.5 Flash/Pro и другие) пришёл из пересказа, не дословно. Для Gemini 2.5 Pro и 2.5 Flash указано устаревание с 1 декабря 2026.
- **Лимиты.** Числа для бесплатного тарифа текстовых моделей на странице не напечатаны: «Rate limits depend on a variety of factors … and can be viewed in Google AI Studio». Известно, что квоты считаются на проект, суточные (RPD) сбрасываются в полночь по тихоокеанскому времени. Числа напечатаны только для Gemini Decision: 200 запросов в минуту, 50 000 токенов в минуту, 10 000 запросов в день.
- **Карта и биллинг.** Для бесплатного уровня не указано. Для перехода на платный нужно сначала настроить биллинг. Уровень Free требует «active project or free trial; some projects need verification».
- **Данные.** На бесплатном уровне стоит «Used to improve our products: Yes», на платном — нет.
- **Регионы** (ЕЭЗ, Великобритания, Швейцария): не указано на прочитанных страницах.

### OpenRouter

- **Лимиты для моделей `:free`** (страница лимитов): менее 10 купленных кредитов — 20 запросов в минуту и 50 в день; не менее 10 купленных кредитов — 20 в минуту и 1000 в день. Те же 50 и 1000 есть в FAQ и на странице цен. Порог в тексте страницы лимитов остался шаблонным местом («{FREE_MODEL_CREDITS_THRESHOLD - 1}»), точное значение порога по этой странице не восстановить.
- **Примеры моделей `:free`** с моментального снимка страницы: `baidu/ernie-5.5-flash-preview:free`, `thinkingmachines/inkling-2-small:free`, `liquid/lfm-3-1.7b:free`, `parallel/decisions-fast:free`. Список меняется, этот снимок неполный.
- **Правила.** «Failed attempts count toward that daily cap» (страница цен). При отрицательном балансе бесплатные модели блокируются, пока не пополнить счёт.
- **Карта.** При регистрации не указано; сказано «create an account and add credits», принимаются карты, AliPay и USDC. В тарифной таблице у Free в строке способов оплаты стоит «No».

### Groq

Источник: страница Organization Limits [console.groq.com/settings/limits](https://console.groq.com/settings/limits) (нужен вход в аккаунт), проверено вручную 12 ноября 2026.

**Цифры ниже — базовые лимиты плана Free. На плане Developer лимиты выше.**

| Модель | RPM | RPD | TPM | TPD |
|---|---|---|---|---|
| `openai/gpt-oss-120b` | 30 | 1000 | 8000 | 200000 |
| `openai/gpt-oss-20b` | 30 | 1000 | 8000 | 200000 |
| `qwen/qwen3.8-27b` | 30 | 1000 | 8000 | 200000 |
| `allam-2-7b` | 30 | 7000 | 6000 | 500000 |
| `whisper-large-v3` (речь в текст) | 20 | 2000 | — | 28800 аудио-секунд в день |
| `canopylabs/orpheus-v1-english` (текст в речь) | 10 | 100 | 1200 | 3600 |

Расшифровка: RPM — запросов в минуту, RPD — в день, TPM — токенов в минуту, TPD — токенов в день.

- **Расхождение с публичной документацией.** Публичная страница [docs/rate-limits](https://console.groq.com/docs/rate-limits) в тексте называет похожую таблицу базовыми лимитами плана Developer и не содержит `allam-2-7b`. Страница Organization Limits, которую смотрел пользователь, показывает те же числа для модели gpt-oss, qwen и whisper как лимиты Free. Какой из двух подписей верить, я проверить не могу (страница Organization Limits требует вход); в этом файле принята версия пользователя. Страница моделей даёт для Developer другие, более высокие числа (например, для `openai/gpt-oss-120b` «250K TPM, 1K RPM»).
- **Карта.** Для Free не указано на странице. Для апгрейда с Free на Developer нужен способ оплаты (карта, банковский счёт США или SEPA).

### DeepSeek

- **Free tier.** На прочитанных официальных страницах бесплатных токенов, пробного баланса и бесплатного тарифа нет.
- **Неясное место.** Страница цен в правилах списания упоминает «granted balance» (используется раньше пополненного) без указания источника, суммы и срока. Это не подтверждённый бесплатный тариф.
- **Лимиты.** Фиксированных RPM и TPM нет, есть лимит одновременных запросов на аккаунт: 2500 (`deepseek-flash`) и 500 (`deepseek-v4-pro`), при превышении HTTP 429. Расширение лимита по заявке «no additional cost».
- **Оплата и карта.** Упомянут «topped-up balance» (предоплата). Минимальная сумма и требование карты не указаны. Страница `platform.deepseek.com` вернула 403, страница FAQ собирается скриптом и не читается, так что регистрационные условия мне неизвестны.

### Kimi (Moonshot)

- **Free tier.** Модель оплаты — «pay-as-you-go basis, with no subscription plan». Бесплатного тарифа или пробного баланса нет.
- **Что есть.** «A minimum recharge of $1 is required to start using the API; when your cumulative recharge reaches $5, you receive a $5 voucher». Ваучер не учитывается в накопленной сумме, срок действия не указан. Файловые API (извлечение текста и хранение) «temporarily free» на неопределённый срок.
- **Лимиты.** Зависят от накопленной суммы пополнений; таблица уровней на странице пустая (загружается скриптом), поэтому RPM, TPM и параллельность по уровням не получены. Лимиты считаются на пользователя, не на ключ, общие для всех моделей; превышение даёт HTTP 429.
- **Оплата.** Для частных пользователей названы WeChat Pay и Alipay, для бизнеса — связь с отделом продаж. Требование банковской карты не указано.

## Источники и дата проверки

Дата проверки всех строк: 12 ноября 2026.

| Сервис | Источник данных |
|---|---|
| Anthropic | [pricing](https://platform.claude.com/docs/en/about-claude/pricing), [rate-limits](https://platform.claude.com/docs/en/api/rate-limits); отсутствие стартовых кредитов проверено вручную на аккаунте пользователя |
| Vercel AI Gateway | [pricing](https://vercel.com/docs/ai-gateway/pricing) (last updated 8 сентября 2026), проверено вручную; карта: [getting-started](https://vercel.com/docs/ai-gateway/getting-started) |
| Google AI Studio | [pricing](https://aistudio.google.com/docs/pricing), [rate-limits](https://aistudio.google.com/docs/rate-limits) |
| OpenRouter | [limits](https://openrouter.ai/docs/api-reference/limits), [FAQ](https://openrouter.ai/docs/faq), [pricing](https://openrouter.ai/pricing) |
| Groq | [Organization Limits](https://console.groq.com/settings/limits) (вручную, нужен вход), [rate-limits](https://console.groq.com/docs/rate-limits), [billing-faqs](https://console.groq.com/docs/billing-faqs) |
| DeepSeek | [pricing](https://api-docs.deepseek.com/quick_start/pricing/), [rate_limit](https://api-docs.deepseek.com/quick_start/rate_limit) |
| Kimi | [limits](https://platform.kimi.ai/docs/pricing/limits), [pricing](https://platform.kimi.ai/docs/pricing/chat), [account-and-payments](https://platform.kimi.ai/docs/guide/account-and-payments) |

## Чему не стоит верить без проверки

- Страницы Google (цены), Anthropic (цены) и каталог Vercel читались не полностью или через пересказ. Такие места помечены «из пересказа» или «не дословно».
- Таблицы лимитов Kimi пришли пустыми, поэтому их цифр здесь нет.
- Условия быстро меняются. Перед использованием откройте ссылку из таблицы и сверьте.
