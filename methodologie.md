Méthodologie de Calcul de la Consommation Énergétique par Token pour une Entreprise
Résumé Exécutif
Ce document fournit une méthodologie complète et robuste pour calculer la consommation énergétique des services d'intelligence artificielle (IA) déployés par une entreprise. Nous détaillerons les formules de calcul de l'énergie exprimées en kilowattheures par token (kWh/token) pour trois profils d'utilisation distincts : la traduction automatique, le chatbot conversationnel, et la génération de contenu (completion). Cette méthodologie s'appuie sur les données officielles des fournisseurs de modèles (OpenAI, Azure, DeepL, Intento) et les résultats de recherches scientifiques publiées.
1. Introduction et Contexte
L'utilisation croissante des modèles de langage de grande taille (LLM) dans les entreprises crée une nécessité urgente de quantifier leur impact énergétique. Selon le rapport du MIT publié en janvier 2025, "The demand for new data centers cannot be met in a sustainable way. The pace at which companies are building new data centers means the bulk of the electricity to power them must come from fossil fuel-based power plants"[1] . Par conséquent, une mesure précise de la consommation énergétique par token devient essentielle pour les entreprises souhaitant optimiser leur empreinte carbone.
2. Limites de l'Analyse
Avant de procéder, il est crucial d'identifier les limites intrinsèques de cette méthodologie et celles des publications sur lesquelles elle s'appuie.
2.1 Limites de la Méthodologie
La quantification de la consommation énergétique des modèles d'IA présente plusieurs défis méthodologiques. D'abord, les fournisseurs de modèles ne divulguent pas systématiquement leurs données énergétiques précises. Les chiffres utilisés dans ce document proviennent donc de trois sources : (1) les déclarations officielles limitées des entreprises, (2) les estimations publiées dans des publications peer-reviewed, et (3) les approximations basées sur l'architecture matérielle et l'utilisation du GPU.
Deuxièmement, la consommation énergétique varie considérablement en fonction de nombreux paramètres non contrôlés : la configuration matérielle du data center, le taux d'utilisation du GPU (qui peut varier de 10 % à 100 %), la technique de quantification utilisée, la longueur effective de l'input et output, et la localisation du data center. Comme l'indique l'étude de 2025 sur le benchmarking énergétique des LLM, "These architectural differences affect throughput and latency, resulting in higher or lower energy consumed per token, but do not impact total system power demand under load"[2].
Troisièmement, le Power Usage Effectiveness (PUE) varie largement entre les data centers. Selon Statista 2024, "data center owners and operators reported an average annual power usage effectiveness (PUE) ratio of 1.56 at their largest data center"[3]. Cependant, les data centers les plus efficaces, comme ceux de Google, atteignent des PUE de 1.09[4], tandis que les installations moins efficaces peuvent atteindre 2.0 ou plus.
Le Power Usage Effectiveness (PUE) mesure l'efficacité énergétique d'un data center en calculant le ratio entre la consommation électrique totale du site et celle uniquement dédiée aux serveurs IT. Un PUE de 1.0 représente l'idéal théorique, où toute l'énergie est utilisée pour le calcul sans pertes (refroidissement, alimentation, etc.), mais cela reste théorique car des pertes sont inévitables en pratique. Plus le PUE est élevé (par exemple >1.5), moins le data center est efficace, indiquant des gaspillages importants en énergie non-productive (https://www.data4group.com/dictionnaire-du-datacenter/qu-est-ce-qu-un-pue/)

2.2 Limites des publications
Les publications académiques quantifiant l'énergie des LLM présentent également des limitations importantes. Comme l'observe l'étude "How Hungry is AI? Benchmarking Energy, Water, and...", "Many current AI energy consumption calculations only include active machine consumption, overlooking several of the critical factors discussed above. As a result, they represent theoretical efficiency instead of true operating efficiency at scale"[5].
De plus, Strubell et al. (2019), dans leur analyse pionnière des émissions carbone de l'entraînement, "estimated carbon emissions from training BERT and GPT-2 by accounting for GPU, CPU, and DRAM power draw alongside PUE adjustments. However, their analysis excludes inference and infrastructural overhead"[6]. Les études ultérieures ont partiellement remédié à cette limitation, mais aucune n'offre une couverture complète de tous les facteurs.
Enfin, la plupart des estimations disponibles concernent l'inférence, tandis que les données d'entraînement restent fragmentaires et spécifiques à chaque entreprise.
3. Définition des Éléments Fondamentaux
3.1 Qu'est-ce qu'un Token ?
Un token est l'unité atomique de traitement dans les modèles de langage. Selon OpenAI : "Tokens are the building blocks of text that OpenAI models process. They can be as short as a single character or as long as a full word, depending on the language and context"[7].
Pour la langue anglaise, les règles empiriques d'OpenAI indiquent : "1 token ≈ 4 characters, 1 token ≈ ¾ of a word, 100 tokens ≈ 75 words, 1–2 sentences ≈ 30 tokens, 1 paragraph ≈ 100 tokens, ~1,500 words ≈ 2,048 tokens"[7]. Ces approximations sont essentielles pour convertir la taille des documents en tokens avant calcul.
Pour les langues non-anglaises, notamment le français, l'allemand et l'espagnol, le ratio peut différer. Comme l'indique la documentation OpenAI : "Tokenization can vary by language. For example, 'Cómo estás' (Spanish for 'How are you') contains 5 tokens for 10 characters. Non-English text often produces a higher token-to-character ratio"[7]. Pour cette analyse, nous utiliserons le facteur de conversion par défaut de 4 caractères par token pour l'anglais et de 3.5 caractères par token pour les langues européennes comme approximation.
3.2 Entrées (Input Tokens) et Sorties (Output Tokens)
Dans l'inférence de modèles, les tokens d'entrée (input tokens) et les tokens de sortie (output tokens) ont généralement des coûts énergétiques différents. Selon la recherche de 2025 sur l'énergie des requêtes ChatGPT, "For an input of 10k tokens and an output of 500 tokens, the total cost increases to around 2.4 watt-hours, and 100k input tokens and 500 output tokens would cost around 40 watt-hours of energy. Note that because of the KV cache, this is an upfront cost"[10].
Le KV cache (Key-Value cache) est un mécanisme d'optimisation utilisé lors de l'inférence autoregressive des transformers, où les clés (keys) et valeurs (values) calculées pour les tokens d'entrée et les tokens précédents sont stockées en mémoire pour éviter leur recalcul à chaque nouvelle génération de token. Cela réduit drastiquement la complexité computationnelle de l'attention, passant d'une recomputation quadratique sur l'ensemble de la séquence à une opération linéaire par nouveau token, expliquant ainsi le coût énergétique "en amont" mentionné pour les longs inputs.
Cette asymétrie s'explique par le mécanisme d'attention quadratique des transformers. Le coût de traitement de l'input évolue quadratiquement, tandis que la génération de tokens de sortie évolue linéairement. Pour les inputs très longs, cette asymétrie devient dominante.
3.3 Latence et Temps de Réponse
La latence API représente le temps entre l'envoi d'une requête et la réception de la première réponse, typiquement mesurée en millisecondes. Selon la documentation sur l'optimisation de la latence, "API latency is measured in milliseconds. Factors that affect it include: Distance between client and server, Network traffic and quality, Network device efficiency, Server processing power"[11].
Pour cette analyse, nous considérerons : (1) la latence réseau (typiquement 50-200 ms pour les appels API cloud), (2) le temps de traitement du serveur (dépendant du modèle et de la charge), et (3) le temps de génération des tokens (latence par token pour les outputs).
Pour caractériser les performances des appels aux modèles de langage, nous nous appuyons sur les métriques standardisées utilisées dans l’industrie et la recherche, notamment dans les benchmarks publics 
OpenRouter https://openrouter.ai/google/gemini-3-flash-preview/performance, llmperf https://github.com/ray-project/llmperf
Hugging Face https://huggingface.co/spaces/optimum/llm-perf-leaderboard.
Trois métriques principales sont retenues :
●	Débit (throughput) : nombre de tokens générés par seconde. Cette métrique permet d’estimer le temps de génération des tokens de sortie et influence directement la consommation énergétique lors de la phase de décodage.
●	Latence au premier token (Time To First Token – TTFT) : temps écoulé entre l’envoi de la requête et la réception du premier token généré. Elle inclut la latence réseau ainsi que la phase de prétraitement (prefill) du modèle.
●	Latence de bout en bout (end-to-end latency) : temps total entre l’envoi de la requête et la réception de la réponse complète. Cette métrique agrège la latence au premier token et le temps de génération de l’ensemble des tokens de sortie.

4. Formule Générale de Calcul de l'Énergie
4.1 Formule Fondamentale
L'énergie consommée par une inférence LLM peut être décomposée selon la formule suivante :
E_total = E_training + E_inference + E_infrastructure
Où :
●	E_training = énergie attribuée à la phase d'entraînement (amortie)
●	E_inference = énergie directe de l'inférence
●	E_infrastructure = frais généraux du data center
4.2 Phase d'Entraînement : Mention et Justification de l'Exclusion
Bien que la phase d'entraînement soit énergétiquement très coûteuse, elle ne doit pas être attribuée à chaque inférence pour les modèles en production. Selon Papineni et al. (2022), "Training remains orders of magnitude more energy- and carbon- intensive than inference"[12]. Cependant, l'énergie d'entraînement doit être amortie sur la durée de vie du modèle.
Par exemple, pour GPT-3, l'étude de Patterson et al. (2021) documentée dans les publications du MIT rapporte : "scientists from Google and the University of California at Berkeley estimated the training process alone consumed 1,287 megawatt hours of electricity (enough to power about 120 average U.S. homes for a year), generating about 552 tons of carbon dioxide"[13]. À titre de comparaison, une requête ChatGPT typique utilise environ 0.3 watt-heure[14], ce qui signifierait qu'il faudrait environ 4.3 millions de requêtes pour égaler le coût d'entraînement de GPT-3.
Pour les modèles plus petits et plus récents, ce ratio est meilleur. De plus, dans un contexte d'API cloud où plusieurs milliers d'utilisateurs partagent le même modèle, le coût d'entraînement par utilisateur devient rapidement négligeable.
Justification de l'exclusion : Pour une analyse opérationnelle de la consommation énergétique d'une entreprise utilisant des API cloud, l'énergie d'entraînement est considérée comme externalisée au fournisseur. L'entreprise cliente paie pour l'inférence, pas pour l'entraînement. Par conséquent, cette méthodologie excluera E_training de ses calculs, mais reconnaît que cette énergie a été consommée antérieurement et en amont.
4.3 Formule Détaillée d'Inférence
L'énergie d'inférence peut être décomposée en deux phases : le prétraitement (prefill) et la génération (decoding).
Pour chaque inférence :
E_inference = (P_GPU × t_compute × η_GPU + P_CPU × t_compute × η_CPU) × PUE_adjust × utilization_rate
Où :
●	P_GPU = puissance nominale du GPU en watts (TDP ou puissance mesurée)
●	P_CPU = puissance du CPU système en watts
●	t_compute = temps de calcul en heures
●	η_GPU, η_CPU = taux d'utilisation réelle des ressources (typiquement 60-80% pour GPU, 20-30% pour CPU)
●	PUE =Power Usage Effectiveness du data center utilisé
●	utilization_rate = taux d'utilisation du serveur (pourcentage du temps où le GPU exécute une inférence)

Analyse unitaire de notre calcul : 
Analyse = [(token / (token/s)) + (token / (token/s))] * [(Watt * sans_unité) + (Watt * sans_unité)] * sans_unité
Analyse = [secondes + secondes] * [Watt + Watt] * sans_unité
Analyse = [secondes] * [Watt] * sans_unité
Analyse = Watt * secondes
Analyse = Joules
4.4 Estimation du Temps de Calcul (t_compute)
Le temps de calcul peut être estimé en fonction du nombre de tokens et du débit du modèle. Pour calculer cette information de temps, on pose le cas de la full self-attention (matrice d’attention calculée entièrement) sans prendre en compte les nouvelles techniques comme la sparse attention, la flash attention ou même la linear attention. On se place dans le “pire cas” y compris dans l’utilisation des modèles les plus récents.
t_compute_prefill = (input_tokens^2 / (throughput/ 3600))
t_compute_decode = (output_tokens / (throughput/ 3600))
Où les débits (throughput) sont exprimés en tokens par seconde et le temps en heures.
5. Données de Base des Fournisseurs de Modèles
5.1 OpenAI (ChatGPT / GPT-5)
OpenAI ne divulgue pas les chiffres énergétiques officiels, mais publie sa tarification de l’API basée sur les tokens. Selon le site officiel des prix d'OpenAI (octobre 2025)[15] :
GPT-5 : Input $1.25 / 1M tokens, Output $10.00 / 1M tokens
GPT-4.1 : Input $2.00 / 1M tokens, Output $8.00 / 1M tokens
Pour l'énergie, les estimations académiques basées sur le benchmarking direct fournissent des données plus utiles. Selon l'étude d'énergie de ChatGPT publiée en février 2025 par Epoch.ai : "We find that typical ChatGPT queries using GPT-4o likely consume roughly 0.3 watt-hours, which is ten times less than the older estimate"[16]. Cette source note également : "According to prices compiled by Artificial Analysis, Llama 3.1 405B costs $3.50 per million output tokens on average, which is more than 10 times more expensive. The cost of renting GPUs is almost certainly the biggest cost of running these APIs, so this suggests that providers need about 10x as many GPUs compared to if they achieved 100% utilization. This means utilization is roughly 10%, increasing the GPUs required, and hence our energy estimate, by 10x"[17].
Cette observation est cruciale : l'utilisation réelle des GPU pour les services d'API cloud est estimée à seulement 10%, ce qui signifie que 90% de la puissance est consommée par des serveurs en attente ou exécutant d'autres tâches. Cela justifie l'ajustement utilization_rate dans notre formule.
Pour GPT-5 spécifiquement, les estimations indépendantes indiquent une consommation beaucoup plus élevée que GPT-4o. Selon l'étude de l'Université de Rhode Island publiée en août 2025 : "Independent research by the University of Rhode Island's AI lab estimates GPT-5 uses approximately 8.6× more energy per query than GPT-4, consuming around 18.35 watt-hours on average, and peaking up to 40 Wh per medium-length response"[18].
5.2 Azure (Microsoft)
Microsoft Azure n'expose pas non plus de données énergétiques directes. Cependant, Microsoft a publié plusieurs articles sur la durabilité des datacenters en décembre 2024 et septembre 2024. Le document "Sustainable by design: Innovating for energy efficiency in AI, part 1" indique : "We use the power of software to drive energy efficiency at every level of the infrastructure stack, from datacenters to servers to silicon"[19]. Microsoft revendique des taux d'utilisation de "80 to 90% utilization at scale"[20] grâce à Project Forge, son système d'ordonnancement basé sur l'IA.
L'étude benchmarking énergétique de 2025 effectue des mesures directes sur les instances Azure avec des GPU H100. Les résultats montrent que les coûts énergétiques d'Azure sont comparables à OpenAI, avec quelques variations selon la configuration[21].
5.3 DeepL (Traduction)
DeepL, basée en Allemagne, a établi des data centers en Islande pour minimiser son impact carbone. Selon son blog de durabilité (décembre 2025) : "DeepL is building a greenhouse gas (GHG) inventory to measure emissions across our operations and value chain. By tracking emissions throughout the business and setting future targets, we take meaningful steps to reduce our environmental impact"[22].
Cependant, DeepL ne publie pas de chiffres précis d'énergie par token. Un article de recherche comparative de 2025 sur la traduction et l'impact environnemental rapporte : "The fine-tuned Gemma-3-4B model achieved performance comparable to GPT-4o and outperformed GPT-4o-mini across all metrics, while consuming approximately 15 times less energy per inference"[23]. Cela suggère que les modèles de traduction spécialisés peuvent être considérablement plus efficaces que les LLM généraux pour la traduction.
5.4 Intento
Intento ne divulgue pas de données énergétiques publiques. Intento opère comme un agrégateur de services MT/IA, routant les requêtes vers divers fournisseurs (OpenAI, Google, DeepL, Azure, etc.). Par conséquent, la consommation énergétique d'Intento dépend entièrement des fournisseurs sous-jacents plus un léger surcoût pour la routage et l'orchestration.
Cas 1 — Utilisation d’un fournisseur unique via Intento
Lorsque le client utilise Intento avec un seul provider explicitement configuré, la consommation énergétique associée à Intento est assimilée à celle du fournisseur sous-jacent.
Dans ce cas :
●	Intento joue un rôle de pass-through (orchestration légère),
●	La consommation énergétique est estimée comme si le client appelait directement le fournisseur.
Formellement :
E_Intento≈E_provider
Cas 2 — Utilisation du Smart Routing (distribution probabiliste)
Lorsque le client utilise la fonctionnalité de Smart Routing d’Intento, les requêtes sont distribuées dynamiquement entre plusieurs fournisseurs selon des critères tels que :
●	le coût,
●	la qualité de sortie,
●	la disponibilité,
●	ou potentiellement, à terme, l’empreinte carbone.
Dans ce cas, la consommation énergétique doit être modélisée comme une espérance pondérée sur l’ensemble des fournisseurs utilisés.
Modélisation probabiliste
Soit un ensemble de fournisseurs :
{P1,P2,…,Pn}
Chaque fournisseur Pi est sélectionné avec une probabilité wi, telle que :
∑wi=1
La consommation énergétique moyenne par requête est alors donnée par :
E_Intento=∑(wi×E_Pi)
où :
●	E_Pi est la consommation énergétique estimée du fournisseur Pi pour une requête donnée (calculée selon la méthodologie décrite dans les sections précédentes),
●	wi est la probabilité de routage vers ce fournisseur.


6. Mix Énergétique et PUE par Pays
6.1 Intensité Carbone de l'Électricité
Le calcul complet de l'impact carbone nécessite de connaître la source d'énergie du data center. Selon l'Agence Européenne de l'Environnement (novembre 2024)[24] :
●	Islande : ~5 gCO₂e/kWh (presque 100% énergie renouvelable)
●	Norvège : 30 gCO₂e/kWh (hydroélectricité abondante)
●	France : ~60 gCO₂e/kWh (mix nucléaire et renouvelable)
●	Allemagne : ~140 gCO₂e/kWh (transition énergétique en cours, part croissante de renouvelables)
●	Pays-Bas : ~200 gCO₂e/kWh (mix diverse)
●	États-Unis (moyenne) : 380-400 gCO₂e/kWh (dépend fortement de l'état)
●	Moyenne mondiale : 481 gCO₂e/kWh[25]
DeepL opérant principalement en Islande et Allemagne, on peut estimer une intensité carbone moyenne de (5 + 140)/2 = 72.5 gCO₂e/kWh pour DeepL.
OpenAI et Azure opèrent dans plusieurs régions, incluant les États-Unis (mix régional ~370-400 gCO₂e/kWh) et des régions avec plus de renouvelables. Une moyenne pondérée par déploiement suggère ~250-300 gCO₂e/kWh.
6.2 Power Usage Effectiveness (PUE) par Région
Selon Mordor Intelligence (août 2025), "Germany's Energy Efficiency Act will prohibit data centers above 1.2 PUE beginning 2027"[26]. Cette regulation sera effectivement plus stricte que la moyenne mondiale.
●	Allemagne (standard nouveau) : PUE 1.2-1.25 (cible réglementaire)
●	Islande (DeepL) : PUE 1.1-1.15 (data centers hautement optimisés)
●	États-Unis (hyperscale) : PUE 1.2-1.4 (entreprises comme Google et Meta atteignent 1.09-1.12, mais moyenne plus haute)
●	Moyenne mondiale 2024 : PUE 1.56[27]
●	Facilities les plus efficaces : PUE 1.1 (Google rapporte 1.09)[28]
Pour les calculs, nous utiliserons : DeepL = 1.15, OpenAI/Azure = 1.3 (moyenne pond
érée des US data centers), Moyenne mondiale = 1.56.
7. Hardware et Puissance
7.1 Consommation Énergétique du GPU
Les GPUs utilisés pour l'inférence LLM varient considérablement. Les plus courants sont :
●	NVIDIA A100 : TDP 250W, puissance opérationnelle typique ~180-200W à 70% d'utilisation
●	NVIDIA H100 : TDP 700W, puissance opérationnelle typique ~500-550W à 70% d'utilisation
●	NVIDIA H200 : TDP 700W, performances améliorées mais consommation similaire
Lors d’une inférence LLM, on distingue généralement deux phases :
Pour la phase de prefill (traitement des inputs), la charge GPU est élevée mais la latence est importante. Pour la phase de decode (génération), la charge GPU est plus faible (chaque GPU génère un token à la fois) mais la latence est critique.
Selon l'étude Infrastructure-aware benchmarking de 2025 : "An A100 can generate up to 72000 tokens per hour, 400W for the A100, 70W for the CPU, and PUE = 1.1, 26 Joules of W consumption per generated token"[29]. Ce chiffre de 26 joules par token décodé (output token) pour une A100 est une référence directe très utile.
Conversion : 26 joules = 26 / 3,600,000 kWh = 0.0000072 kWh/token ≈ 7.2 microWh/token pour la génération avec A100 et PUE=1.1.
Pour les H100 (environ 3-4 fois plus puissants mais 3-4 fois plus puissants en consommation), on peut estimer ~24 microWh/token pour le décodage et ~ 216000 tokens par heure.
Il est important de souligner que ces chiffres constituent des ordres de grandeur issus de benchmarks académiques, et non des valeurs fixes ou contractuelles. Le domaine de l’inférence LLM est en forte évolution, avec des gains rapides en performance énergétique.
À titre illustratif, NVIDIA met en avant des améliorations significatives de l’efficacité énergétique avec ses nouvelles architectures B200, notamment lorsqu’elles sont combinées à des modèles ouverts optimisés comme Mistral. Ces avancées montrent que, à qualité équivalente, l’énergie consommée par token peut être fortement réduite grâce à des architectures GPU plus efficientes, des optimisations mémoire et des modèles mieux adaptés à la tâche: https://developer.nvidia.com/blog/nvidia-accelerated-mistral-3-open-models-deliver-efficiency-accuracy-at-any-scale/
Google n'est pas en reste et propose une approche différente avec ses propres puces, les TPUs. Leur dernière version, "Trillium", est conçue spécifiquement pour l'IA et réussit à être 67% plus économe en énergie que la précédente, comme ils l'expliquent sur leur blog (https://cloud.google.com/blog/products/compute/introducing-trillium-6th-gen-tpus). En plus du matériel, Google a optimisé son logiciel "JetStream" pour que des modèles comme Mixtral fonctionnent trois fois plus vite, ce qui réduit mécaniquement la facture électrique pour chaque mot généré (voir les détails : https://cloud.google.com/blog/products/compute/ai-hypercomputer-inference-updates-for-google-cloud-tpu-and-gpu).
7.2 Puissance CPU et Overhead Système
Selon le papier HotCarbon de 2024 sur le cycle de vie des LLM : "While specialized AI engines account for the lion's share of power consumption in generative AI, general purpose CPUs incur non-trivial embodied carbon overheads"[30]. Le CPU système consomme typiquement 70-100W pour un serveur de datacenter, soit environ 15-30% de la consommation totale du GPU + CPU.
8. Formules de Calcul de l’énergie due à l’infrastructure réseau
L'exclusion de la consommation réseau dans le calcul de l'empreinte énergétique d'une requête IA s'explique principalement par la nature non déterministe et mutualisée d'Internet, qui rend toute estimation précise extrêmement complexe voire impossible à l'échelle d'une simple interaction. Contrairement à un GPU dont on peut mesurer la consommation exacte pendant les millisecondes d'une inférence, le transport de la donnée traverse une multitude de routeurs et de câbles (souvent transfrontaliers) dont l'infrastructure est allumée en permanence, qu'il y ait du trafic ou non. Attribuer une part de cette consommation "fixe" à une requête unique relève de l'arbitraire, d'autant que le chemin parcouru change dynamiquement et que l'intensité carbone de l'électricité varie à chaque frontière traversée. De plus, pour les modèles de langage (LLM), l'énergie nécessaire au calcul (inférence sur des puces H100/A100) est souvent plusieurs ordres de grandeur supérieure à celle du transport de quelques kilooctets de texte, rendant la part du réseau statistiquement négligeable dans le bilan final.
Pourquoi le réseau est souvent exclu des calculs
La difficulté méthodologique majeure réside dans l'absence de proportionnalité énergétique des équipements réseau : un routeur consomme presque autant d'énergie à vide qu'à pleine charge. Isoler le coût marginal d'une requête individuelle nécessite donc des hypothèses de modélisation lourdes (diviser la conso totale par le volume de données mondial) qui ne reflètent pas la réalité physique instantanée.
●	L'infrastructure est une "boîte noire" : Il est impossible de savoir si votre requête vers un serveur aux USA est passée par un câble sous-marin spécifique ou a été routée via Londres ou Paris, empêchant l'application d'un mix électrique national précis.

●	La volatilité temporelle : La consommation réelle dépend de la congestion du réseau à la milliseconde près (heure de pointe vs nuit), une donnée inaccessible pour l'utilisateur final de l'API.

●	Le ratio Signal/Calcul : Dans l'IA générative, on envoie très peu de données (un "prompt" textuel) pour déclencher un calcul massif. Contrairement au streaming vidéo (beaucoup de données, peu de calcul), ici le coût énergétique est concentré dans le datacenter, rendant l'approximation "Réseau = 0" acceptable pour simplifier l'analyse.
8. Formules de Calcul par Profil d'Utilisation
8.1 Profil 1 : Traduction (TRANSLATION)
Caractéristiques :
●	Input : contenu du topic (topic_size)
●	Output : contenu traduit (≈ topic_size, car la traduction ne change pas drastiquement la longueur)
●	Exemple : DeepL ou système de traduction spécialisé
tokens_input = topic_size / 4 (ou len(enc.encode(text)) d’après tiktoken pour les modèles OpenAI)
Lorsque le texte est disponible (ex. échantillonnage interne, logs de contenu accessibles), nous calculons le nombre de tokens exact à l’aide du tokenizeur BPE tiktoken d’OpenAI, en utilisant l’encodage correspondant au modèle (encoding_for_model). Cela permet de capturer la tokenisation réelle (non-linéaire) et d’éviter une hypothèse fixe caractères/token.
Plus simplement, pour évaluer le volume de texte (en "tokens"), nous utilisons deux approches selon les données disponibles. Si nous avons accès au texte lui-même et au modèle utilisé (cas général du projet), nous utilisons l'outil de calcul précis d'OpenAI pour obtenir le chiffre exact. En revanche, si nous ne connaissons que le nombre de caractères, nous appliquons une estimation simple et reconnue : un token équivaut environ à 4 caractères pour l’explication théorique.
Lorsque le texte n’est pas disponible et que seules des métriques agrégées (ex. topic_size en caractères) sont accessibles, nous utilisons une approximation cohérente avec l’anglais, langue majoritaire chez Fluid Topics : 1 token ≈ 4 caractères.

tokens_output = topic_size / 4
PUE_deepl = PUE_islande = 1.15
η_CPU = 30-15% selon HotCarbon
η_CPU + η_GPU = 1 car on se place dans le pire cas de consommation (Réseau Dense pas MoE)
utilization_rate = 1 car chaque requête doit porter le “reste à gagner” de l’utilization_rate

E_translation = E__training + E_inference + E_infra
E_translation = ~0 + E_inference + ~0
E_translation = (P_GPU × t_compute × η_GPU + P_CPU × t_compute × η_CPU) × PUE × utilization_rate
E_translation = t_compute ×  (P_GPU × η_GPU + P_CPU × η_CPU) × PUE_islande ×  1 
E_translation = (t_compute_prefill + t_compute_decode)  ×  [(700 × 1-(30+15)/200 ) + (100+70)/2 × (30+15)/200] × 1.15 
E_translation = (input_tokens^2 / (throughput/ 3600))+ (output_tokens / (throughput/ 3600)) ×  [(700 × 1-(30+15)/200 ) + (100+70)/2 × (30+15)/200 ] × 1.15 
E_translation_per_token = ((input_tokens^2 / (216000 / 3600)) + (output_tokens / (216000 / 3600)) ×  [(700 × 1-(30+15)/200 ) + (100+70)/2 × (30+15)/200 ] × 1.15 
E_translation = ((input_tokens^2 / 60) + (output_tokens / 60)) * [(700 * (1 - 0.225)) + (85 * 0.225)] * 1.15
E_translation = ((input_tokens^2 + output_tokens) / 60) * [542.5 + 19.125] * 1.15
E_translation = ((input_tokens^2 + output_tokens) / 60) * 561.625 * 1.15
E_translation = ((input_tokens^2 + output_tokens) / 60) * 645.87
E_translation = (input_tokens^2 + output_tokens) * 10.7645
8.2 Profil 2 : Chatbot (CHATBOT)
Caractéristiques :
●	Input : n topics (1 à 50) + prompt systemchatbot
●	Output : réponse générée (200-400 caractères typiquement, soit ~57-114 tokens)
●	Exemple : GPT-4o ou équivalent (cas général) ou GPT-5.x (cas optimisé récent)
tokens_input = (sum_all(topic_sizes) + prompt_size) / 4
tokens_output ≈ 300 tokens (moyenne 200-400 caractères)
PUE_gpt = PUE_us = 1.3
η_CPU = 30-15% selon HotCarbon
η_CPU + η_GPU = 1 car on se place dans le pire cas de consommation (Réseau Dense pas MoE)
utilization_rate = 1 car chaque requête doit porter le “reste à gagner” de l’utilization_rate

E_chatbot = E__training + E_inference + E_infra
E_chatbot = ~0 + E_inference + ~0
E_chatbot = (P_GPU × t_compute × η_GPU + P_CPU × t_compute × η_CPU) × PUE × utilization_rate
E_chatbot = ((input_tokens^2 / (216000 / 3600)) + (output_tokens / (216000 / 3600)) × (700 × (1-0.225)  + 85 × 0.225) × 1.3 × 1
E_chatbot = ((((sum_all(topic_sizes) + prompt_size) / 3.5)^2 / (216000 / 3600)) + (300  / (216000 / 3600)) × (700 × (1-2.225)  + 85 × 0.225) × 1.3 × 1
E_chatbot = (((sum_all(topic_sizes) + prompt_size) / 4)^2 / (60)) + 3650,5625

8.3 Profil 3 : Génération / Completion (COMPLETION)
Caractéristiques :
●	Input : 1 topic + prompt
●	Output : contenu généré (200-400 caractères)
●	Modèle : GPT-4o ou GPT-5.x
tokens_input = (topic_size + prompt_size) / 4
tokens_output ≈ 300 tokens (moyenne 200-400 caractères)
PUE_chatpgt = PUE_us = 1.3
η_CPU = 30-15% selon HotCarbon
η_CPU + η_GPU = 1 car on se place dans le pire cas de consommation (Réseau Dense pas MoE)
utilization_rate = 1 car chaque requête doit porter le “reste à gagner” de l’utilization_rate

E_completion = E__training + E_inference + E_infra
E_completion = ~0 + E_inference + ~0
E_completion = (P_GPU × t_compute × η_GPU + P_CPU × t_compute × η_CPU) × PUE × utilization_rate
E_completion = ((topic_size + prompt_size) / 4)^2 / (60)) + 3650,5625

9. Différences Entre les Profils et Justifications
9.1 Traduction vs. Génération / Chatbot
La traduction est 15 à 50 fois plus efficace énergétiquement que la génération de contenu avec un LLM généraliste. Selon l'étude comparative de 2025 : "The fine-tuned Gemma-3-4B model achieved performance comparable to GPT-4o and outperformed GPT-4o-mini across all metrics, while consuming approximately 15 times less energy per inference"[35].
Raisons scientifiques :
1.	Tâche discriminative vs. générative : Selon le papier "Watts Driving the Cost of AI Deployment?" (2024), "Generative tasks are more energy- and carbon-intensive compared to discriminative tasks"[36]. La traduction, en tant que tâche plus structurée avec une espace de sortie plus restreinte (vocabulaire traduit), est énergétiquement plus efficace que la génération libérée générale.
2.	Taille et spécialisation du modèle : Les modèles de traduction dédiés (7B à 13B paramètres) surpassent les LLM généraux de 175B+ paramètres pour la tâche de traduction. La recherche montre que l'utilisation du modèle approprié pour la tâche (scaling law) réduit la consommation de 27.8% en moyenne[37].
3.	Architectures optimisées : Les systèmes MT modernes utilisent des techniques comme la quantification, Mixture of Experts (MoE), et Flash Attention, réduisant la consommation d'énergie de 85% selon les sources sectorielles[38].
9.2 Chatbot vs. Completion
Le chatbot traite plusieurs topics en input (jusqu'à 50) tandis que completion n'en traite qu'un. De plus, le chatbot maintient une session et peut faire plusieurs tours, accumulant les coûts.
Différences clés :
1.	Longueur d'input : Pour n=50 topics, tokens_input peut atteindre 18,750 tokens, soit 9x plus qu'une completion (625 tokens). Le coût de prefill croît quadratiquement[39], donc le coût d'input du chatbot est ~20-30x supérieur.
2.	Nombre d'inférences : Une conversation chatbot implique généralement plusieurs tours (turn-taking), tandis que completion est généralement single-turn.
3.	Latence requise : Le chatbot nécessite une latence faible pour une bonne UX conversationnelle, ce qui peut nécessiter des configurations GPU sous-utilisées (réservation de capacité).
10. Données Spécifiques des Fournisseurs (Résumé)
10.1 OpenAI (GPT-5 / GPT-4o)
Localisation : États-Unis (multiple régions), quelques data centers en Europe
Intensité carbone : ~300 gCO₂e/kWh (moyenne pondérée US/EU)
PUE : ~1.3 (estimation basée sur l'utilisation 10% rapportée)
Consommation par requête :
●	GPT-4o (requête moyenne ~3000 tokens) : 0.3 Wh = 0.3 × 10^-3 kWh
●	GPT-5 (requête moyenne ~3000 tokens) : 18.35 Wh (estimation indépendante) = 18.35 × 10^-3 kWh
Ratio énergétique : GPT-5 consomme ~61× plus d'énergie que GPT-4o par requête, malgré une meilleure qualité.
10.2 Azure
Localisation : États-Unis, Europe, autres régions
Intensité carbone : ~280 gCO₂e/kWh (mix régional avec priorité aux renouvelables)
PUE : ~1.25 (Microsoft revendique 80-90% d'utilisation via Project Forge[40])
Consommation par requête : Comparable à OpenAI pour modèles similaires, avec variations liées à la configuration régionale
10.3 DeepL
Localisation : Islande + Allemagne
Intensité carbone : ~72.5 gCO₂e/kWh (très bas grâce à l'Islande)
PUE : ~1.15 (data centers d'Islande très efficaces)
Consommation par requête :
●	Traduction (DeepL propriétaire) : 0.0005-0.002 Wh = 0.5-2 microWh (estimation basée sur 15x plus efficace que GPT-4o pour MT)
Avantage carbone : Même avec une consommation énergétique 10x plus faible (per task), l'intensité carbone extrêmement faible de l'Islande (5 gCO₂/kWh) fait que DeepL produit ~7-10x moins de CO₂ qu'OpenAI pour une traduction équivalente.
10.4 Intento
Localisation : Dépend du routage (peut être n'importe quel fournisseur)
PUE / Intensité carbone : Agrégat pondéré de tous les fournisseurs backend
Surcoût : +5-15% d'énergie/latence pour orchestration et routage
12. Outils de Mesure en Production
La mesure de la consommation énergétique des LLM en production est essentielle pour valider les estimations théoriques. Plusieurs outils et frameworks existent.
12.1 ETHIC AI
Une autre ressource pertinente sur la mesure de la consommation énergétique des systèmes d’IA en production est le rapport “Calculating AI’s Energy Use” publié par EthicAI (https://ethicai.net/calculating-ais-energy-use). Ce document propose une méthodologie détaillée pour évaluer objectivement l’énergie utilisée par des modèles d’IA dans des contextes réels, en intégrant des éléments tels que les charges GPU effectives, l’efficacité des infrastructures (PUE), et la variabilité des data centers. Il complète les outils existants comme CodeCarbon et Electricity Maps en fournissant un cadre d’analyse pour relier des mesures empiriques à des estimations globales, ce qui est utile pour valider et contextualiser les estimations de consommation énergétique dans notre méthodologie.
12.2 CodeCarbon
CodeCarbon (https://codecarbon.io/)est une bibliothèque Python open-source qui suit la consommation électrique et les émissions de carbone pendant l'exécution du code. Selon la documentation de CodeCarbon et son utilisation dans les papiers académiques[41] :
Avantages :
●	Intégration facile avec du code Python existant
●	Suivi en temps réel de la consommation d'électricité
●	Utilise des données d'intensité carbone par région (Electricity Maps API)
●	Pas de dépendances matérielles externes requises
Inconvénients :
●	Mesures imprécises si le processus n'est pas la charge dominante du système
●	Dépend de la précision des drivers GPU pour mesurer la consommation réelle (PyNVML pour NVIDIA) mais concerne les providers et non FluidTopics qui ne possède pas de GPU
●	N'inclut pas naturellement le PUE du data center sauf si configuré manuellement
●	Limité aux exécutions locales ou à SSH (pas d'API cloud native)
Limites :
CodeCarbon mesure le GPU directement mais pas l'infrastructure globale. Selon le papier How Hungry is AI : "Many current AI energy consumption calculations only include active machine consumption, overlooking several of the critical factors discussed above. As a result, they represent theoretical efficiency instead of true operating efficiency at scale"[42]. CodeCarbon par défaut ne mesure que la consommation active du GPU.
12.3 Green Algorithms Initiative
La Green Algorithms Initiative fournit une calculatrice en ligne basée sur des formules empiriques publiées. Elle prend en compte :
●	Type de processeur et puissance
●	Région du data center et intensité carbone
●	PUE estimé
●	Durée d'exécution
Avantages :
●	Simple et accessible sans intégration de code
●	Ajuste automatiquement pour PUE et régions
Inconvénients :
●	Interface web, pas d'API pour l'automatisation
●	Estimations moins précises que CodeCarbon (pas de mesure réelle du GPU)
●	Nécessite l'entrée manuelle des paramètres
12.3 Electricity Maps API
Electricity Maps (https://www.electricitymaps.com/  anciennement WattTime) fournit une API pour l'intensité carbone en temps réel par région. Plusieurs publications l'utilisent[43].
Avantages :
●	Données de carbone en temps réel par région géographique
●	Peut être combinée avec CodeCarbon
●	API publique bien documentée https://app.electricitymaps.com/developer-hub/api/getting-started#introduction
●	Utile pour l'optimisation temporelle/spatiale des workloads
Inconvénients :
●	Requiert une clé API (tier gratuit limité)
●	Nécessite de connaître la localisation du data center
●	N'inclut pas automatiquement la mesure de l'énergie (doit être couplée à CodeCarbon ou autre)
12.4 Google Sustainable AI Initiative Framework
Google a publié en août 2025 une "comprehensive methodology for measuring the energy, emissions, and water impact of Gemini prompts"[44]. Cette approche mesure :
●	Énergie active du serveur (TPU/GPU)
●	Infrastructure data center (incluant refroidissement)
●	Matériel système (CPU, DRAM, stockage)
●	Utilisation de l'eau (souvent oubliée, environ 0.12 mL d'eau par requête médiane Gemini)
Google rapporte que cette méthodologie holistique produit des estimations très différentes de celles basées uniquement sur le GPU.
Avantages :
●	Méthodologie complète et peer-reviewed
●	Inclut infrastructure et overhead
●	Rend compte de l'inefficacité réelle (non théorique)
Inconvénients :
●	Spécifique à l'écosystème Google (TPU, infrastructure interne)
●	Pas facilement transférable à d'autres fournisseurs/hardware
●	Require accès à des données internes non disponibles pour les clients cloud externes
12.5 Hugging Face AI Energy Score
Hugging Face a lancé en 2024 le AI Energy Score, un benchmark standardisé pour comparer l'efficacité énergétique des modèles[45].
Avantages :
●	Leaderboard public des modèles par efficacité énergétique
●	Benchmark standardisé avec 10 tâches
●	Inclut modèles open-source et propriétaires
●	Rating intuitif (1-5 stars)
Inconvénients :
●	Basé sur des inférences locales (pas représentatif du déploiement cloud)
●	Requiert que le modèle soit téléchargeable (exclut les APIs cloud propriétaires)
●	Variabilité selon le hardware d'évaluation
12.6 Microsoft Sustainable AI Design Framework
Microsoft fournit une documentation et des recommandations pour l'IA durable sur Azure[46]. Cependant, pas d'outil public spécifique pour mesurer per-query comme Google ou CodeCarbon.
13. Implémentation Python
Voici un exemple complet d'implémentation pour mesurer et calculer la consommation énergétique des profils d'utilisation de l'entreprise.
import os
import sys
import time
import json
from datetime import datetime
from typing import Dict, List, Tuple
import requests
class AIEnergyCalculator:
"""
Calculates energy consumption and CO2 emissions for different AI profiles
(Translation, Completion, Chatbot) based on token usage and provider data.
"""
def __init__(self, provider: str = "openai", region: str = "us"):
    """
    Initialize the calculator with provider and region information.
    
    Args:
        provider: One of 'openai', 'azure', 'deepl', 'intento'
        region: Region code for carbon intensity lookup
    """
    self.provider = provider.lower()
    self.region = region.lower()
    
    # Provider configurations (kWh per token)
    self.provider_config = {
        'openai': {
            'gpt4o': {
                'input_energy_microwhbyt': 0.0001,  # micro Wh per token input
                'output_energy_microwhpertoken': 0.0002,
                'energy_per_query_wh': 0.3,  # median for 3000 token query
                'pue': 1.3,
                'carbon_intensity': 300  # gCO2/kWh
            },
            'gpt5': {
                'energy_per_query_wh': 18.35,
                'pue': 1.3,
                'carbon_intensity': 300
            }
        },
        'azure': {
            'default': {
                'energy_per_query_wh': 0.32,  # slightly higher than OpenAI
                'pue': 1.25,
                'carbon_intensity': 280
            }
        },
        'deepl': {
            'default': {
                'energy_per_query_wh': 0.001,  # 1/300 de GPT-4o
                'pue': 1.15,
                'carbon_intensity': 72.5  # Iceland + Germany average
            }
        }
    }
    
    # Token conversion factors (characters per token)
    self.token_factors = {
        'english': 4.0,
        'french': 3.5,
        'german': 3.5,
        'spanish': 3.5,
        'multilingual': 3.7  # average
    }
    
    # Carbon intensity by region (gCO2e/kWh) - 2024/2025 estimates
    self.carbon_intensity = {
        'iceland': 5,
        'norway': 30,
        'france': 60,
        'germany': 140,
        'netherlands': 200,
        'us': 380,
        'us-west': 350,
        'us-east': 400,
        'eu-avg': 250,
        'world': 481
    }

def characters_to_tokens(self, characters: int, language: str = 'english') -> int:
    """Convert character count to token count based on language."""
    factor = self.token_factors.get(language.lower(), self.token_factors['english'])
    return int(characters / factor)

def tokens_to_characters(self, tokens: int, language: str = 'english') -> int:
    """Convert token count to character count."""
    factor = self.token_factors.get(language.lower(), self.token_factors['english'])
    return int(tokens * factor)

def get_carbon_intensity(self, region: str = None) -> float:
    """Get carbon intensity for a region in gCO2e/kWh."""
    if region is None:
        region = self.region
    return self.carbon_intensity.get(region.lower(), self.carbon_intensity['world'])

def calculate_translation(self, 
                          topic_size_chars: int,
                          language: str = 'french') -> Dict:
    """
    Calculate energy for translation profile.
    
    Args:
        topic_size_chars: Size of content to translate in characters
        language: Language of content (for token conversion)
    
    Returns:
        Dictionary with energy consumption and CO2 calculations
    """
    # Convert to tokens
    tokens = self.characters_to_tokens(topic_size_chars, language)
    # Input + Output for translation
    total_tokens = tokens * 2
    
    # Use DeepL as baseline for translation (15x more efficient than GPT-4o)
    # Estimate: 0.3 Wh / 15 ≈ 0.02 Wh for DeepL, but more precisely:
    # Energy per 1000 characters
    energy_wh = (topic_size_chars / 1000) * 0.051  # 51.5 Wh per 5000 chars from example
    energy_kwh = energy_wh / 1000
    
    carbon_intensity = self.get_carbon_intensity('iceland' if self.provider == 'deepl' else self.region)
    co2_grams = energy_kwh * carbon_intensity
    
    return {
        'profile': 'translation',
        'topic_size_chars': topic_size_chars,
        'tokens': total_tokens,
        'energy_wh': energy_wh,
        'energy_kwh': energy_kwh,
        'energy_kwh_scientific': f'{energy_kwh:.2e}',
        'carbon_intensity_gco2_kwh': carbon_intensity,
        'co2_grams': co2_grams,
        'co2_kg': co2_grams / 1000,
        'timestamp': datetime.now().isoformat()
    }

def calculate_completion(self,
                         topic_size_chars: int,
                         prompt_size_chars: int = 500,
                         model: str = 'gpt4o',
                         language: str = 'french') -> Dict:
    """
    Calculate energy for completion profile (single-turn generation).
    
    Args:
        topic_size_chars: Size of input content
        prompt_size_chars: Size of system prompt
        model: Model selection ('gpt4o' or 'gpt5')
        language: Language for token conversion
    
    Returns:
        Dictionary with energy consumption and CO2 calculations
    """
    tokens_input = self.characters_to_tokens(topic_size_chars + prompt_size_chars, language)
    tokens_output = self.characters_to_tokens(300, language)  # avg 200-400 chars output
    
    # Energy based on provider and model
    if self.provider == 'openai':
        if model.lower() == 'gpt5':
            energy_wh = 18.35 * (tokens_input + tokens_output) / 3000  # scale to token count
        else:  # gpt4o
            energy_wh = 0.3 * (tokens_input + tokens_output) / 3000
    elif self.provider == 'azure':
        energy_wh = 0.32 * (tokens_input + tokens_output) / 3000
    else:  # default
        energy_wh = 0.3 * (tokens_input + tokens_output) / 3000
    
    energy_kwh = energy_wh / 1000
    carbon_intensity = self.get_carbon_intensity()
    co2_grams = energy_kwh * carbon_intensity
    
    return {
        'profile': 'completion',
        'model': model,
        'topic_size_chars': topic_size_chars,
        'prompt_size_chars': prompt_size_chars,
        'tokens_input': tokens_input,
        'tokens_output': tokens_output,
        'tokens_total': tokens_input + tokens_output,
        'energy_wh': energy_wh,
        'energy_kwh': energy_kwh,
        'energy_kwh_scientific': f'{energy_kwh:.2e}',
        'carbon_intensity_gco2_kwh': carbon_intensity,
        'co2_grams': co2_grams,
        'co2_kg': co2_grams / 1000,
        'timestamp': datetime.now().isoformat()
    }

def calculate_chatbot(self,
                      topics_list: List[int],
                      prompt_size_chars: int = 500,
                      language: str = 'french') -> Dict:
    """
    Calculate energy for chatbot profile (multi-topic conversational).
    
    Args:
        topics_list: List of topic sizes in characters [topic1_chars, topic2_chars, ...]
        prompt_size_chars: Size of system prompt
        language: Language for token conversion
    
    Returns:
        Dictionary with energy consumption and CO2 calculations
    """
    n_topics = len(topics_list)
    total_input_chars = sum(topics_list) + prompt_size_chars
    tokens_input = self.characters_to_tokens(total_input_chars, language)
    tokens_output = self.characters_to_tokens(300, language)  # avg response
    
    # Chatbot uses GPT-4o by default
    # Base energy is ~0.3 Wh for 3000 tokens, scaled for actual token count
    energy_wh = 0.3 * (tokens_input + tokens_output) / 3000
    
    energy_kwh = energy_wh / 1000
    carbon_intensity = self.get_carbon_intensity()
    co2_grams = energy_kwh * carbon_intensity
    
    return {
        'profile': 'chatbot',
        'n_topics': n_topics,
        'topic_sizes_chars': topics_list,
        'total_input_chars': total_input_chars,
        'prompt_size_chars': prompt_size_chars,
        'tokens_input': tokens_input,
        'tokens_output': tokens_output,
        'tokens_total': tokens_input + tokens_output,
        'energy_wh': energy_wh,
        'energy_kwh': energy_kwh,
        'energy_kwh_scientific': f'{energy_kwh:.2e}',
        'carbon_intensity_gco2_kwh': carbon_intensity,
        'co2_grams': co2_grams,
        'co2_kg': co2_grams / 1000,
        'timestamp': datetime.now().isoformat()
    }

def compare_providers(self,
                      topic_size_chars: int,
                      profile: str = 'completion') -> List[Dict]:
    """
    Compare energy consumption across different providers for the same task.
    
    Args:
        topic_size_chars: Size of content in characters
        profile: 'translation', 'completion', or 'chatbot'
    
    Returns:
        List of comparison results for each provider
    """
    providers_to_test = ['openai', 'azure', 'deepl']
    results = []
    
    for prov in providers_to_test:
        calc = AIEnergyCalculator(provider=prov, region=self.region)
        
        if profile == 'translation':
            result = calc.calculate_translation(topic_size_chars)
        elif profile == 'completion':
            result = calc.calculate_completion(topic_size_chars)
        elif profile == 'chatbot':
            result = calc.calculate_chatbot([topic_size_chars])
        else:
            continue
        
        results.append(result)
    
    return results

def aggregate_daily_usage(self, profile_usage: Dict[str, int]) -> Dict:
    """
    Aggregate energy consumption for a full day of usage.
    
    Args:
        profile_usage: Dictionary with daily counts
                      {'translation_requests': N, 'completion_requests': N, 'chatbot_sessions': N,
                       'avg_topic_size': chars, 'avg_topics_per_chatbot': N}
    
    Returns:
        Aggregated daily energy and CO2
    """
    daily_results = {
        'translation': {
            'requests': profile_usage.get('translation_requests', 0),
            'avg_topic_size': profile_usage.get('avg_topic_size', 2000),
        },
        'completion': {
            'requests': profile_usage.get('completion_requests', 0),
            'avg_topic_size': profile_usage.get('avg_topic_size', 2000),
        },
        'chatbot': {
            'sessions': profile_usage.get('chatbot_sessions', 0),
            'avg_topics': profile_usage.get('avg_topics_per_chatbot', 5),
            'avg_topic_size': profile_usage.get('avg_topic_size', 2000),
        }
    }
    
    total_energy_kwh = 0
    total_co2_grams = 0
    
    # Translation
    for _ in range(daily_results['translation']['requests']):
        result = self.calculate_translation(daily_results['translation']['avg_topic_size'])
        total_energy_kwh += result['energy_kwh']
        total_co2_grams += result['co2_grams']
    
    # Completion
    for _ in range(daily_results['completion']['requests']):
        result = self.calculate_completion(daily_results['completion']['avg_topic_size'])
        total_energy_kwh += result['energy_kwh']
        total_co2_grams += result['co2_grams']
    
    # Chatbot
    for _ in range(daily_results['chatbot']['sessions']):
        topics = [daily_results['chatbot']['avg_topic_size']] * daily_results['chatbot']['avg_topics']
        result = self.calculate_chatbot(topics)
        total_energy_kwh += result['energy_kwh']
        total_co2_grams += result['co2_grams']
    
    return {
        'period': 'daily',
        'translation_requests': daily_results['translation']['requests'],
        'completion_requests': daily_results['completion']['requests'],
        'chatbot_sessions': daily_results['chatbot']['sessions'],
        'total_energy_kwh': total_energy_kwh,
        'total_energy_mwh': total_energy_kwh / 1000,
        'total_co2_grams': total_co2_grams,
        'total_co2_kg': total_co2_grams / 1000,
        'total_co2_metric_tons': total_co2_grams / 1_000_000,
        'timestamp': datetime.now().isoformat()
    }

Example usage
if name == "main":
# Initialize calculator for OpenAI in US
calc_openai = AIEnergyCalculator(provider='openai', region='us')
# Calculate translation profile
trans_result = calc_openai.calculate_translation(topic_size_chars=5000, language='french')
print("Translation Profile (OpenAI):")
print(json.dumps(trans_result, indent=2))
print()

# Calculate completion profile with GPT-4o
comp_result = calc_openai.calculate_completion(
    topic_size_chars=2000,
    prompt_size_chars=500,
    model='gpt4o',
    language='french'
)
print("Completion Profile (OpenAI GPT-4o):")
print(json.dumps(comp_result, indent=2))
print()

# Calculate completion profile with GPT-5
comp_gpt5_result = calc_openai.calculate_completion(
    topic_size_chars=2000,
    prompt_size_chars=500,
    model='gpt5',
    language='french'
)
print("Completion Profile (OpenAI GPT-5):")
print(json.dumps(comp_gpt5_result, indent=2))
print()

# Calculate chatbot profile
chatbot_result = calc_openai.calculate_chatbot(
    topics_list=[1500, 1500, 2000, 1000, 1500],
    prompt_size_chars=500,
    language='french'
)
print("Chatbot Profile (5 topics):")
print(json.dumps(chatbot_result, indent=2))
print()

# Compare providers for translation
print("Provider Comparison for Translation (5000 chars):")
comparison = calc_openai.compare_providers(5000, profile='translation')
for result in comparison:
    print(f"  {result['profile'].upper()}: {result['energy_kwh']:.6f} kWh, {result['co2_grams']:.2f} grams CO2")
print()

# Aggregate daily usage
daily_usage = {
    'translation_requests': 100,
    'completion_requests': 50,
    'chatbot_sessions': 20,
    'avg_topic_size': 2000,
    'avg_topics_per_chatbot': 5
}
daily_result = calc_openai.aggregate_daily_usage(daily_usage)
print("Daily Aggregated Usage (OpenAI, US region):")
print(json.dumps(daily_result, indent=2))

Références
[1] MIT News, "Explained: Generative AI's environmental impact", janvier 2025, https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117
[2] How Hungry is AI? Benchmarking Energy, Water, and Environmental Impact of LLM Inference Across 30 Model Systems, 2025, arxiv.org/html/2505.09598v1
[3] Statista, "Data center average annual PUE worldwide 2024", avril 2025
[4] WEF Forum, "How data centres can avoid doubling their energy use", décembre 2025, https://www.weforum.org/stories/2025/12/data-centres-and-energy-demand/
[5] Google Cloud Blog, "Measuring the environmental impact of AI inference", août 2025, https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference/
[6] How Hungry is AI? op. cit. https://arxiv.org/pdf/2505.09598
[7] OpenAI Help Center, "What are tokens and how to count them?", septembre 2025, https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
[10] Epoch.ai, "How much energy does ChatGPT use?", février 2025, https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
[11] Inference.net, "Optimizing Latency vs. Response Time in AI Deployment", mai 2025
[12] Papineni et al., "Watts Driving the Cost of AI Deployment?", 2024, arxiv.org/html/2311.16863v3
[13] MIT News, op. cit.
[14] Epoch.ai, op. cit.
[15] OpenAI Pricing, https://openai.com/api/pricing/, octobre 2025
[16] Epoch.ai, op. cit.
[17] Ibid.
[18] "GPT-5 Energy Efficiency vs GPT-4: AI's Green Leap Forward", août 2025, https://aiinsighttalks.com/gpt-5-energy-efficiency-vs-gpt-4-ais-green-leap-forward/
[19] Microsoft Cloud Blog, "Sustainable by design: Innovating for energy efficiency in AI, part 1", septembre 2024
[20] Ibid.
[21] How Hungry is AI? op. cit.
[22] DeepL Sustainability, "Harnessing AI the sustainable way", décembre 2025, https://www.deepl.com/en/sustainability/environment
[23] Castaldo et al., "Balancing Translation Quality and Environmental Impact", 2025, ceur-ws.org/Vol-4112/19_main_long.pdf
[24] EEA, "Greenhouse gas emission intensity of electricity generation in Europe", novembre 2025
[25] Statista, "Power sector carbon intensity worldwide by country 2023", juillet 2024
[26] Mordor Intelligence, "Europe Data Center Power Market Size & Share Analysis", août 2025
[27] Statista, op. cit.
[28] WEF Forum, op. cit.
[29] Infrastructure-aware benchmarking paper, 2024, https://archives.iw3c2.org/www2022/wp-content/uploads/Sponsors/WWW2022-Technology-Innovation-Institute.pdf
[30] "Towards Carbon-efficient LLM Life Cycle", HotCarbon 2024, https://hotcarbon.org/assets/2024/pdf/hotcarbon24-final154.pdf
[31] Epoch.ai, op. cit.
[32] Ibid.
[33] Ibid.
[34] Ibid.
[35] Castaldo et al., op. cit.
[36] Papineni et al., op. cit.
[37] "Reducing the World AI Energy Consumption Through Model Selection and Scaling", 2024, arxiv.org/html/2510.01889v1
[38] DeepL Bridges, "Green AI in Translation: Why DeepL's Efficiency Matters More Than Ever", novembre 2025
[39] Epoch.ai, op. cit.
[40] Microsoft Cloud Blog, op. cit.
[41] Clara Na, "Energy and Carbon Considerations of Fine-Tuning BERT", https://clarasna.com/assets/pdf/energy_and_carbon.pdf
[42] Google Cloud Blog, op. cit.
[43] Clagtee, "Assessing the Energy Impact and Carbon Footprint of AI", https://clagtee.fi.mdp.edu.ar/full-papers-search-engine/papers/ID071.pdf
[44] Google Cloud Blog, op. cit.
[45] Hugging Face, "AI Energy Score", https://huggingface.github.io/AIEnergyScore/, décembre 2024
[46] Microsoft Learn, "Sustainable AI design for workloads on Azure", https://learn.microsoft.com/en-us/azure/well-architected/sustainability/sustainable-ai-design

