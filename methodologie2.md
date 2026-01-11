Méthodologie Complète : Calcul de la Consommation Énergétique par Token pour Fluid Topics
Table des matières
Méthodologie Complète : Calcul de la Consommation Énergétique par Token pour Fluid Topics	1
1. Introduction et Contexte Métier	3
Justification et Contexte CSRD / ESG	3
2. Architecture Générale de la Méthodologie Fluid Topics	4
3. Fondamentaux : Topics, Sessions et Profils IA	4
3.1 Notion de Topic	4
3.2 Notion de Session Utilisateur	4
3.3 Profils IA	5
4. Types de Contenus et Périmètre d'Analyse	5
4.1 Contenus Gérés par Fluid Topics	5
4.2 Paramètres Clés pour la Simulation	5
5. Les Trois Profils IA : Caractéristiques et Fonctionnement	5
5.1 Profil 1 : Translation (Traduction)	5
5.2 Profil 2 : Completion (Génération Simple)	6
5.3 Profil 3 : Chatbot (Génération Conversationnelle)	6
5.4 Résumé Comparatif des Trois Profils	6
6. Conversion des Caractères en Tokens	7
6.1 Hypothèse Standard et Justification	7
6.2 Variation Selon la Langue	7
7. Calcul du Volume de Tokens par Profil	8
7.1 Formules de Calcul des Tokens	8
7.2 Agrégation au Niveau Quotidien	8
8. Exploitation des Données Analytics Fluid Topics	8
8.1 Données Collectées par Fluid Topics	8
8.2 Passage au Niveau Client	9
9. Méthodologie de Calcul de la Consommation Énergétique par Token	9
Méthodologie de Calcul de la Consommation Énergétique par Token pour une Entreprise	9
Résumé Exécutif	9
9.1 Introduction et Contexte	9
9.2 Limites de l'Analyse	10
9.2.1 Limites de la Méthodologie	10
9.2.2 Limites des Publications Scientifiques	10
9.3 Définition des Éléments Fondamentaux	11
9.3.1 Qu'est-ce qu'un Token ?	11
9.3.2 Entrées (Input Tokens) et Sorties (Output Tokens)	11
9.3.3 Latence et Temps de Réponse	12
9.4 Formule Générale de Calcul de l'Énergie	12
9.4.1 Formule Fondamentale	12
9.4.2 Phase d'Entraînement : Mention et Justification de l'Exclusion	12
9.4.3 Formule Détaillée d'Inférence	13
9.4.4 Estimation du Temps de Calcul (t_compute)	14
9.5 Données de Base des Fournisseurs de Modèles	14
9.5.1 OpenAI (ChatGPT / GPT-5)	14
9.5.2 Azure (Microsoft)	14
9.5.3 DeepL (Traduction)	15
9.5.4 Intento	15
9.6 Mix Énergétique et PUE par Pays	16
9.6.1 Intensité Carbone de l'Électricité	16
9.6.2 Power Usage Effectiveness (PUE) par Région	16
9.7 Hardware et Puissance	17
9.7.1 Consommation Énergétique du GPU	17
9.7.2 Puissance CPU et Overhead Système	18
9.8 Formules de Calcul de l'Énergie due à l'Infrastructure Réseau	18
9.9 Formules de Calcul par Profil d'Utilisation	19
9.9.1 Profil 1 : Traduction (TRANSLATION)	19
9.9.2 Profil 2 : Chatbot (CHATBOT)	20
9.9.3 Profil 3 : Génération / Completion (COMPLETION)	21
9.10 Différences Entre les Profils et Justifications	21
9.10.1 Traduction vs. Génération / Chatbot	21
9.10.2 Chatbot vs. Completion	22
9.11 Données Spécifiques des Fournisseurs (Résumé)	22
9.11.1 OpenAI (GPT-5 / GPT-4o)	22
9.11.2 Azure	23
9.11.3 DeepL	23
9.11.4 Intento	23
10. Outils de Mesure en Production	23
10.1 ETHIC AI	23
10.2 CodeCarbon	24
10.3 Green Algorithms Initiative	24
10.4 Electricity Maps API	24
10.5 Google Sustainable AI Initiative Framework	25
11. Implémentation Pratique et Avantages Commerciaux	25
11.1 Implémentation Proposée	25
11.2 Avantages pour Fluid Topics	25
12. Recommandations Futures et Limitations	26
12.1 Validation de l'Énergie par Token pour les Fournisseurs	26
12.2 Conversion Token-Caractères pour Langues Européennes	26
12.3 Optimisation des Tokens et Routage Intelligent	26
12.4 Configuration des Data Centers par Fournisseur	26
12.5 Données Fictives pour Testing	27
12.6 Format d'Intégration	27
13. Conclusion	27
Références	27

1. Introduction et Contexte Métier
La plateforme Fluid Topics intègre de plus en plus de fonctionnalités basées sur l'intelligence artificielle et le machine learning. Ces services, qu'il s'agisse de traduction automatique, de génération de contenu ou d'assistants conversationnels, offrent une valeur immédiate aux utilisateurs. Cependant, chaque interaction avec un modèle de langage de grande taille (LLM) consomme de l'énergie et génère une empreinte carbone. Pour Fluid Topics, il est devenu essentiel de quantifier, documenter et communiquer cet impact de manière transparente et justifiée scientifiquement.
La méthodologie présentée dans ce document répond à trois objectifs majeurs. En premier lieu, elle permet d'estimer la consommation énergétique de chaque profil IA déployé dans la plateforme, en fonction des données réelles collectées par les analytics. En second lieu, elle fournit aux clients une transparence sur leur consommation d'énergie et d'émissions de carbone liées à l'utilisation de l'IA, un argument de vente majeur pour les organisations soumises à la directive CSRD (Corporate Sustainability Reporting Directive) ou sensibles aux enjeux ESG (Environmental, Social and Governance). En troisième lieu, elle offre à Fluid Topics des leviers pour optimiser et piloter ses impacts environnementaux, que ce soit en ajustant les modèles utilisés, en améliorant l'efficacité des prompts, ou en proposant des budgets énergétiques par client.
Justification et Contexte CSRD / ESG
La CSRD (Directive 2022/2464 de l'Union Européenne) impose aux entreprises concernées de publier des informations détaillées et vérifiables sur leurs impacts environnementaux, sociaux et de gouvernance[1]. Elle vise à renforcer la transparence des entreprises sur leurs impacts, améliorer la comparabilité et la fiabilité des données extra-financières, et intégrer les enjeux environnementaux et sociaux dans la stratégie d'entreprise.
Le cadre ESG (Environmental, Social and Governance) regroupe l'ensemble des critères extra-financiers utilisés par les entreprises, les investisseurs et les parties prenantes pour évaluer la durabilité globale d'une organisation[2]. Comprendre cet enjeu à un objectif double pour Fluid Topics : offrir une valeur commerciale directe à nos clients sensibles à ces enjeux, et contribuer à une IA plus durable et responsable. En proposant des outils de transparence énergétique, nous nous positionnons comme leader en matière de responsabilité environnementale dans le secteur de la gestion documentaire.
2. Architecture Générale de la Méthodologie Fluid Topics
La méthodologie repose sur une chaîne logique claire. À partir des actions des utilisateurs dans Fluid Topics, notamment la consultation de contenus et l'activation de fonctionnalités IA, on estime d'abord le volume de tokens traités par les modèles. Ce volume est ensuite multiplié par des facteurs énergétiques spécifiques au fournisseur et au profil IA, ce qui permet de calculer la consommation énergétique en kilowatt-heures (kWh) ou en watt-heures (Wh). Enfin, en multipliant cette consommation par l'intensité carbone de la source d'énergie du data center, on obtient l'empreinte carbone en équivalent CO₂ (gCO₂e).
La beauté de cette approche réside dans sa modularité. Elle permet de passer du niveau granulaire (une requête, un utilisateur) au niveau agrégé (tous les clients d'une région, tous les jours). Elle facilite également les comparaisons : combien consomme la traduction comparée à la génération ? Quel fournisseur est le plus efficace énergétiquement ? Ces questions peuvent être répondues avec les mêmes données et formules, simplement appliquées à différents sous-ensembles.
3. Fondamentaux : Topics, Sessions et Profils IA
3.1 Notion de Topic
Dans Fluid Topics, un topic est l'unité fondamentale de contenu. Une publication (article ou book) contient un ou plusieurs topics. Lorsqu'un utilisateur consulte du contenu ou demande une action IA, celle-ci porte généralement sur un ou plusieurs topics. Chaque topic possède une taille moyenne mesurable en caractères, ce qui sera crucial pour estimer le nombre de tokens traités.
3.2 Notion de Session Utilisateur
Une session utilisateur représente la période durant laquelle un utilisateur spécifique consulte du contenu dans Fluid Topics. Selon la documentation Fluid Topics, « lorsqu'un utilisateur utilise Fluid Topics, le système définit une session pendant laquelle il consulte du contenu, généralement un ou plusieurs topics »[3]. Cette session peut impliquer la consultation d'un seul topic ou de plusieurs topics sur une période donnée.
Il est important de noter que toutes les sessions n'impliquent pas nécessairement une interaction avec des services IA. L'IA n'est sollicitée que si un profil IA est activé et disponible. Sur les 213 portails suivis dans notre portefeuille, seuls 70 génèrent des appels IA, ce qui montre que l'activation des fonctionnalités IA est sélective et bien ciblée selon les besoins métier spécifiques.
3.3 Profils IA
Le cœur de la méthodologie repose sur la distinction entre trois types de profils IA, chacun ayant ses propres caractéristiques en termes de données d'entrée (input), de données de sortie (output) et de consommation énergétique. Ces trois profils seront détaillés dans la section 5.
4. Types de Contenus et Périmètre d'Analyse
4.1 Contenus Gérés par Fluid Topics
Fluid Topics gère quatre catégories principales de contenus. Les publications incluent d'une part les articles et d'autre part les books. Les documents non structurés constituent une deuxième catégorie. Enfin, les attachments (pièces jointes) constituent une quatrième catégorie.
Pour cette méthodologie, sont inclus dans le périmètre d'analyse tous les contenus qui sont traduits ou traités par des services IA. Les contenus qui ne sont ni traduits ni traités par l'IA sont explicitement exclus du périmètre. Cette délimitation claire permet de concentrer l'effort d'estimation sur les activités qui génèrent effectivement une consommation énergétique.
4.2 Paramètres Clés pour la Simulation
Pour simuler et estimer la consommation énergétique à travers le portefeuille client de Fluid Topics, on utilise plusieurs paramètres-clés. Le paramètre « topic_size » représente la taille moyenne d'un topic, mesurée en caractères. Le paramètre « book_topic_number » représente le nombre moyen de topics par book. De manière similaire, « article_topic_number » représente le nombre moyen de topics par article. Enfin, « unstructured_document_size » mesure la taille moyenne d'un document non structuré, également en caractères.
5. Les Trois Profils IA : Caractéristiques et Fonctionnement
5.1 Profil 1 : Translation (Traduction)
Le profil Translation est utilisé pour la traduction automatique de contenu. Le système traite un topic à la fois. Les données d'entrée (input) correspondent au contenu intégral du topic, mesuré en caractères. Les données de sortie (output) correspondent au texte traduit, dont la taille est généralement comparable à celle du texte source, car la traduction ne modifie pas drastiquement la longueur globale du contenu.
Un exemple typique serait l'utilisation de DeepL ou d'un système de traduction spécialisé via une API. L'avantage majeur de ce profil est son efficacité énergétique. Les modèles dédiés à la traduction sont généralement plus compacts et plus optimisés que les modèles de langage généralistes, ce qui réduit significativement la consommation énergétique.
5.2 Profil 2 : Completion (Génération Simple)
Le profil Completion est utilisé pour la génération simple et non conversationnelle de contenu. Le système traite un topic à la fois, enrichi d'un prompt fourni par l'utilisateur ou défini par la plateforme. Les données d'entrée correspondent donc à la taille du topic plus la taille du prompt. Les données de sortie sont limitées à un texte généré de courte à moyenne longueur, typiquement entre 200 et 400 caractères.
Un exemple serait un résumé généré automatiquement d'un article, ou une description courte générée pour un contenu donné. Comparé à la traduction, ce profil implique une génération créative plus coûteuse énergétiquement, car le modèle doit parcourir l'espace des possibilités plutôt que de mapper un texte source vers une langue cible.
5.3 Profil 3 : Chatbot (Génération Conversationnelle)
Le profil Chatbot est utilisé pour la génération conversationnelle et multi-tour. Contrairement aux deux autres profils, le chatbot peut traiter entre un et cinquante topics simultanément. Les données d'entrée incluent l'ensemble de ces topics plus un ou plusieurs prompts (généralement au moins deux dans les interactions normales, mais pouvant être plus dans les modes agent avancés). Les données de sortie correspondent à la réponse générée, typiquement entre 200 et 400 caractères, similaire au profil Completion.
Le chatbot introduit une complexité supplémentaire car il implique une session stateful, où le contexte de la conversation doit être maintenu et enrichi au fil des tours. De plus, le fait de traiter plusieurs topics augmente significativement le volume de données d'entrée, ce qui impacte la consommation énergétique, surtout en raison de la nature quadratique du coût de traitement des inputs dans les architectures transformer.
5.4 Résumé Comparatif des Trois Profils
Aspect
Translation
Completion
Chatbot
Nombre de topics
1
1
1-50
Taille d'input typique
topic_size
topic_size + prompt
n × topic_size + np × prompt
Taille d'output typique
topic_size (traduit)
200-400 caractères
200-400 caractères
Modèle recommandé
DeepL, systèmes MT spécialisés
GPT-4o, Claude 3
GPT-4o, Claude 3
Efficacité énergétique
Très élevée (15-50x GPT)
Modérée
Modérée


6. Conversion des caractères en Tokens (Partie fini par Alexandre G. le 09/01/2026)

Dans la plateforme Fluid Topics, les contenus manipulés (topics, documents, prompts) sont naturellement mesurés en nombre de caractères. En revanche, les fournisseurs de modèles de langage (OpenAI, Azure, DeepL, etc.) facturent et dimensionnent leurs services en fonction du nombre de tokens traités. Une étape essentielle de la méthodologie consiste donc à convertir les tailles de contenus exprimées en caractères en un volume estimé de tokens.
Cette conversion est nécessaire car Fluid Topics ne dispose pas, à ce stade, du détail exact de la tokenisation réalisée par chaque fournisseur pour chaque appel. La méthodologie repose ainsi sur des hypothèses standardisées, reconnues dans la littérature et suffisamment robustes pour fournir des ordres de grandeur exploitables à l’échelle industrielle.

6.1 Hypothèse Standard et Justification
L’hypothèse principale retenue est la suivante : un token correspond en moyenne à quatre caractères. Cette approximation est largement utilisée dans l’écosystème des modèles de langage, notamment par OpenAI via son tokeniseur de référence tiktoken, basé sur des méthodes de type Byte Pair Encoding (BPE).
Cette hypothèse repose sur plusieurs éléments. Tout d’abord, pour la langue anglaise, un token correspond généralement à une fraction de mot ou à un mot court, ce qui conduit à une moyenne proche de quatre caractères, espaces inclus. Ensuite, la majorité des modèles étudiés dans cette méthodologie (OpenAI, Azure OpenAI) sont entraînés et optimisés principalement pour l’anglais, qui constitue également une langue très majoritaire dans les usages clients de Fluid Topics. Enfin, cette approximation est cohérente avec les pratiques d’outils de référence comme CodeCarbon ou avec les ordres de grandeur fournis dans la documentation officielle d’OpenAI.
Du point de vue méthodologique, ce choix permet de garantir une conversion simple, reproductible et compréhensible, sans dépendre d’implémentations spécifiques à chaque modèle ou fournisseur.
Dans la suite de la méthodologie, cette hypothèse de conversion est utilisée de manière cohérente pour l’ensemble des profils IA, afin de garantir la comparabilité des résultats entre usages et fournisseurs.
6.2 Variation Selon la Langue
Il est important de noter que le ratio caractères/token n’est pas strictement constant et dépend de la langue considérée. Pour certaines langues européennes comme le français, l’allemand ou l’espagnol, plusieurs études montrent que le nombre de caractères par token peut être légèrement inférieur, généralement compris entre trois et trois virgule cinq caractères par token.
Cependant, dans une logique de cohérence globale et de simplicité opérationnelle, la méthodologie proposée retient par défaut la conversion standard basée sur l’anglais. Ce choix est justifié par la prédominance de cette langue dans les modèles utilisés et dans les usages observés chez Fluid Topics. Il permet également d’éviter une multiplication de règles spécifiques qui complexifierait inutilement l’implémentation.
Cette hypothèse pourra toutefois être affinée dans le futur si Fluid Topics souhaite introduire des coefficients spécifiques par langue ou par client, notamment pour des portails majoritairement non anglophones.

7. Calcul du Volume de Tokens par Profil
7.1 Formules de Calcul des Tokens
Pour chaque appel IA, le nombre total de tokens est calculé comme la somme des tokens d’entrée et des tokens de sortie.
Pour la Traduction :
Dans le cas du profil Traduction, l’entrée correspond au contenu du topic à traduire, et la sortie correspond au texte traduit. Comme la traduction ne modifie généralement pas de manière significative la longueur du texte, on considère que le nombre de tokens en sortie est du même ordre de grandeur que celui en entrée, d’où : 
tokens_input = topic_size / 4
tokens_output = topic_size / 4 (hypothèse : la taille en caractères reste similaire après traduction)
total_tokens = tokens_input + tokens_output
Pour la Completion :
Pour le profil Completion, l’entrée est constituée du contenu du topic auquel s’ajoute un prompt, tandis que la sortie correspond à un texte généré de longueur limitée. Cette génération est volontairement bornée (quelques centaines de caractères, avec 300 choisis dans les formules dans le cas d’une génération courte) afin de refléter les usages réels de Fluid Topics : 
tokens_input = (topic_size + prompt_size) / 4
tokens_output ≈ 300 (estimation pour une génération courte)
total_tokens = tokens_input + tokens_output
Pour le Chatbot :
Enfin, pour le profil Chatbot, l’entrée peut inclure plusieurs topics ainsi que plusieurs prompts liés au contexte conversationnel. Le volume de tokens d’entrée est donc potentiellement beaucoup plus élevé, tandis que la sortie reste généralement comparable à celle d’une completion classique.
tokens_input = (n × topic_size + np × prompt_size) / 4, où n est le nombre de topics (1 à 50) et np est le nombre de prompts (généralement 2 ou plus)
tokens_output ≈ 300
total_tokens = tokens_input + tokens_output
Ces formules permettent d’obtenir une estimation cohérente du volume de tokens consommés par appel, adaptée aux différents usages IA proposés par la plateforme.
7.2 Agrégation au Niveau Quotidien
Pour exploiter ces calculs à l’échelle de la plateforme, les volumes de tokens sont ensuite agrégés sur une base quotidienne. Concrètement, pour chaque jour, on comptabilise le nombre d’appels réalisés pour chaque profil IA, on multiplie ce nombre par le coût moyen en tokens d’un appel de ce profil, puis on additionne l’ensemble.
Cette agrégation quotidienne est essentielle pour Fluid Topics, car elle permet d’analyser les variations de consommation dans le temps, d’identifier des pics d’usage et de relier directement l’activité des utilisateurs à des indicateurs énergétiques et carbone exploitables dans une démarche RSE.

8. Exploitation des Données Analytics Fluid Topics
La méthodologie repose fortement sur les données déjà collectées par Fluid Topics via ses outils d’analytics. L’objectif est de s’appuyer sur des données existantes, fiables et facilement accessibles, sans introduire de contraintes techniques excessives.
8.1 Données Collectées par Fluid Topics
Fluid Topics collecte notamment le nombre de sessions utilisateur, le nombre de consultations par type de contenu, ainsi que l’utilisation des différents profils IA au fil du temps. Ces données ne fournissent pas directement le nombre de tokens consommés, mais elles constituent une base solide pour l’estimation.
En combinant ces métriques avec les tailles moyennes des contenus (topics, documents) et les hypothèses de conversion définies précédemment, il devient possible d’estimer de manière indirecte mais cohérente le volume total de tokens traités par la plateforme.
8.2 Passage au Niveau Client
Une utilisation avancée de la méthodologie consiste à passer du niveau global (tous les clients) au niveau client spécifique. Si on peut extraire des analytics de la répartition des appels IA par profil (combien d'appels Translation, Completion et Chatbot pour un client donné), on peut calculer la consommation énergétique spécifique à chaque client. La formule est directe : pour un client donné et un jour donné, on comptabilise le nombre d'appels de chaque profil, on multiplie par le coût moyen en tokens du profil, et on obtient le nombre total de tokens consommés ce jour-là. Ce chiffre peut ensuite être fourni automatiquement au client dans l'espace d'administration de son portail, offrant ainsi une transparence directe sur sa consommation.

9. Méthodologie de Calcul de la Consommation Énergétique par Token
Cette section présente la méthodologie détaillée du calcul de la consommation énergétique en fonction du nombre de tokens traités. Elle s'appuie sur les contenus des documents sources, en gardant exactement le contenu du fichier « Méthodologie Énergie par Token » intégré ci-dessous.
Méthodologie de Calcul de la Consommation Énergétique par Token pour une Entreprise
9.1 Introduction et Contexte
L’augmentation rapide de l’usage des modèles de langage en entreprise rend indispensable une quantification précise de leur impact énergétique. Dans le cas de Fluid Topics, cette problématique est d’autant plus importante que les services d’IA reposent sur des infrastructures externes, sur lesquelles l’entreprise n’a pas de contrôle direct.
La méthodologie proposée vise donc à estimer la consommation énergétique associée à l’inférence des modèles, à partir du nombre de tokens traités. Elle s’appuie sur des ordres de grandeur issus de publications scientifiques, de benchmarks publics et des informations communiquées par les fournisseurs de services cloud.
Nous détaillerons les formules de calcul de l'énergie exprimées en kilowattheures par token (kWh/token) pour trois profils d'utilisation distincts : la traduction automatique, le chatbot conversationnel, et la génération de contenu (completion).
9.2 Limites de l'Analyse
Avant de détailler les calculs, il est nécessaire de souligner les limites inhérentes à ce type d’approche.
9.2.1 Limites de la Méthodologie
La quantification de la consommation énergétique des modèles d'IA présente plusieurs défis méthodologiques. La principale limite réside dans l’opacité des fournisseurs de modèles, qui ne publient pas de données énergétiques précises et standardisées. Les valeurs utilisées dans cette méthodologie reposent donc sur des estimations issues de la littérature et de benchmarks, et non sur des mesures directes réalisées par Fluid Topics. Ainsi, les chiffres utilisés dans ce document proviennent donc de trois sources : (1) les déclarations officielles limitées des entreprises, (2) les estimations publiées dans des publications peer-reviewed, et (3) les approximations basées sur l'architecture matérielle et l'utilisation du GPU.
Par ailleurs, la consommation énergétique réelle dépend de nombreux paramètres variables et que nous ne contrôlons pas, tels que le taux d’utilisation des GPU (qui peut varier de 10 % à 100 %), la configuration matérielle des data centers ou encore les optimisations internes mises en place par les fournisseurs (Informations tirées de l'étude de 2025 sur le benchmarking énergétique des LLM, « These architectural differences affect throughput and latency, resulting in higher or lower energy consumed per token, but do not impact total system power demand under load »[7]). La méthodologie vise donc à fournir des ordres de grandeur cohérents plutôt qu’une mesure exacte à l’unité près.
Deuxièmement, la consommation énergétique varie considérablement en fonction de nombreux paramètres non contrôlés : la configuration matérielle du data center, le taux d'utilisation du GPU ), la technique de quantification utilisée, la longueur effective de l'input et output, et la localisation du data center. 
Troisièmement, le Power Usage Effectiveness (PUE) varie largement entre les data centers (Selon Statista 2024, « data center owners and operators reported an average annual power usage effectiveness (PUE) ratio of 1.56 at their largest data center »[8]). Cependant, les data centers les plus efficaces, comme ceux de Google, atteignent des PUE de 1.09[9], tandis que les installations moins efficaces peuvent atteindre 2.0 ou plus.
Le Power Usage Effectiveness (PUE) mesure l'efficacité énergétique d'un data center en calculant le ratio entre la consommation électrique totale du site et celle uniquement dédiée aux serveurs IT. Un PUE de 1.0 représente l'idéal théorique, où toute l'énergie est utilisée pour le calcul sans pertes (refroidissement, alimentation, etc.), mais cela reste théorique car des pertes sont inévitables en pratique. Plus le PUE est élevé (par exemple >1.5), moins le data center est efficace, indiquant des gaspillages importants en énergie non-productive[10].
9.2.2 Limites des Publications Scientifiques
Les études scientifiques existantes présentent elles aussi des limites, notamment le fait que certaines ne prennent en compte que la consommation active du matériel de calcul, sans intégrer l’ensemble des coûts liés à l’infrastructure : son refroidissement, alimentation et autres actions liées à son entretien (D’après les études « How Hungry is AI? Benchmarking Energy, Water, and... », « Many current AI energy consumption calculations only include active machine consumption, overlooking several of the critical factors discussed above. As a result, they represent theoretical efficiency instead of true operating efficiency at scale »[11] et Strubell et al. (2019), dans leur analyse pionnière des émissions carbone de l'entraînement, « estimated carbon emissions from training BERT and GPT-2 by accounting for GPU, CPU, and DRAM power draw alongside PUE adjustments. However, their analysis excludes inference and infrastructural overhead »[12]). De plus, les résultats peuvent rapidement devenir obsolètes en raison de l’évolution rapide des architectures matérielles et logicielles.
Enfin, la plupart des estimations disponibles concernent l'inférence, tandis que les données d'entraînement restent fragmentaires et spécifiques à chaque entreprise.
9.3 Définition des Éléments Fondamentaux
9.3.1 Qu'est-ce qu'un Token ?
Un token est l’unité de base utilisée par les modèles de langage pour traiter le texte. Il peut correspondre à un mot entier, à une partie de mot, ou à un caractère, selon le contexte et la langue. La tokenisation est propre à chaque modèle, ce qui explique la nécessité de recourir à des approximations dans un contexte industriel. D’après OpenAI, les tokens sont les bases pour construire les textes que les modèles d’OpenAI processent (« Tokens are the building blocks of text that OpenAI models process. They can be as short as a single character or as long as a full word, depending on the language and context »[13])
Pour la langue anglaise, les règles empiriques d'OpenAI indiquent : « 1 token ≈ 4 characters, 1 token ≈ ¾ of a word, 100 tokens ≈ 75 words, 1–2 sentences ≈ 30 tokens, 1 paragraph ≈ 100 tokens, ~1,500 words ≈ 2,048 tokens »[13]. Ces approximations sont essentielles pour convertir la taille des documents en tokens avant calcul.
Pour les langues non-anglaises, notamment le français, l'allemand et l'espagnol, le ratio peut différer. Comme l'indique la documentation OpenAI : « Tokenization can vary by language. For example, 'Cómo estás' (Spanish for 'How are you') contains 5 tokens for 10 characters. Non-English text often produces a higher token-to-character ratio »[13]. Pour cette analyse, nous utiliserons le facteur de conversion par défaut de 4 caractères par token pour l'anglais et de 3.5 caractères par token pour les langues européennes comme approximation.
9.3.2 Entrées (Input Tokens) et Sorties (Output Tokens)
Dans l'inférence de modèles, les tokens d'entrée (input tokens) et les tokens de sortie (output tokens) ont généralement des coûts énergétiques différents. Le traitement des tokens d’entrée est plus coûteux, car il implique le calcul complet des mécanismes d’attention (coût de traitement de l’input évolue quadratiquement, tandis que la génération de tokens de sortie évolue linéairement). À l’inverse, la génération des tokens de sortie est généralement moins coûteuse, car elle s’appuie sur des mécanismes de cache qui évitent de recalculer l’ensemble du contexte à chaque étape.
Cette distinction est essentielle pour comprendre pourquoi des usages comme le chatbot, qui impliquent de longues entrées, sont beaucoup plus énergivores que des usages plus simples comme la traduction.
Selon la recherche de 2025 sur l'énergie des requêtes ChatGPT, « For an input of 10k tokens and an output of 500 tokens, the total cost increases to around 2.4 watt-hours, and 100k input tokens and 500 output tokens would cost around 40 watt-hours of energy. Note that because of the KV cache, this is an upfront cost »[14].
Le KV cache (Key-Value cache) est un mécanisme d'optimisation utilisé lors de l'inférence autoregressive des transformers, où les clés (keys) et valeurs (values) calculées pour les tokens d'entrée et les tokens précédents sont stockées en mémoire pour éviter leur recalcul à chaque nouvelle génération de token. Cela réduit drastiquement la complexité computationnelle de l'attention, expliquant ainsi le coût énergétique « en amont » mentionné pour les longs inputs.
9.3.3 Latence et Temps de Réponse
La latence correspond au temps nécessaire pour obtenir une réponse après l’envoi d’une requête à un modèle (typiquement mesurée en millisecondes). Elle dépend à la fois de la latence réseau, de la charge du serveur et du temps de génération des tokens (Selon la documentation sur l'optimisation de la latence, « API latency is measured in milliseconds. Factors that affect it include: Distance between client and server, Network traffic and quality, Network device efficiency, Server processing power »[15]). Si la latence n’est pas directement un indicateur énergétique, elle est étroitement liée au temps de calcul, et donc à la consommation d’énergie.
Dans cette méthodologie, la latence est prise en compte de manière indirecte à travers l’estimation du temps de calcul nécessaire pour traiter un certain volume de tokens. Cela permet de relier les performances perçues par l’utilisateur aux impacts énergétiques sous-jacents.
Pour cette analyse, nous considérerons : 
La latence réseau (typiquement 50-200 ms pour les appels API cloud)
Le temps de traitement du serveur (dépendant du modèle et de la charge)
Le temps de génération des tokens (latence par token pour les outputs).
Pour caractériser les performances des appels aux modèles de langage, nous nous appuyons sur les métriques standardisées utilisées dans l'industrie et la recherche, notamment dans les benchmarks publics OpenRouter, llmperf et Hugging Face[16].
Trois métriques principales sont retenues :
Débit (throughput) : nombre de tokens générés par seconde. Cette métrique permet d'estimer le temps de génération des tokens de sortie et influence directement la consommation énergétique lors de la phase de décodage.
Latence au premier token (Time To First Token – TTFT) : temps écoulé entre l'envoi de la requête et la réception du premier token généré. Elle inclut la latence réseau ainsi que la phase de prétraitement (prefill) du modèle.
Latence de bout en bout (end-to-end latency) : temps total entre l'envoi de la requête et la réception de la réponse complète. Cette métrique agrège la latence au premier token et le temps de génération de l'ensemble des tokens de sortie.
9.4 Formule Générale de Calcul de l'Énergie (Partie fini par Corentin M le 08/01/2026)
9.4.1 Formule Fondamentale
L'énergie consommée par une inférence LLM peut être décomposée selon la formule suivante :
E_total = E_training + E_inference + E_infrastructure
Où :
E_training = énergie attribuée à la phase d'entraînement (amortie)
E_inference = énergie directe de l'inférence
E_infrastructure = frais généraux du data center
9.4.2 Phase d'Entraînement : Mention et Justification de l'Exclusion
Bien que la phase d'entraînement soit énergétiquement très coûteuse, elle ne doit pas être attribuée à chaque inférence pour les modèles en production. Selon Papineni et al. (2022), « Training remains orders of magnitude more energy- and carbon- intensive than inference »[17]. Cependant, l'énergie d'entraînement doit être amortie sur la durée de vie du modèle.
Par exemple, pour GPT-3, l'étude de Patterson et al. (2021) documentée dans les publications du MIT rapporte : « scientists from Google and the University of California at Berkeley estimated the training process alone consumed 1,287 megawatt hours of electricity (enough to power about 120 average U.S. homes for a year), generating about 552 tons of carbon dioxide »[18]. À titre de comparaison, une requête ChatGPT typique utilise environ 0.3 watt-heure[19], ce qui signifierait qu'il faudrait environ 4.3 millions de requêtes pour égaler le coût d'entraînement de GPT-3.
Pour les modèles plus petits et plus récents, ce ratio est meilleur. De plus, dans un contexte d'API cloud où plusieurs milliers d'utilisateurs partagent le même modèle, le coût d'entraînement par utilisateur devient rapidement négligeable.
Justification de l'exclusion : Ici pour une analyse opérationnelle de la consommation énergétique d'une entreprise utilisant des API cloud, l'énergie d'entraînement est considérée comme externalisée au fournisseur. L'entreprise cliente paie pour l'inférence, pas pour l'entraînement. Par conséquent, cette méthodologie exclura E_training de ses calculs, mais reconnaît que cette énergie a été consommée antérieurement et en amont.
9.4.3 Formule Détaillée d'Inférence
L'énergie d'inférence peut être décomposée en deux phases : le prétraitement (prefill) et la génération (decoding).
Pour chaque inférence :
E_inference = (P_GPU × t_compute × η_GPU + P_CPU × t_compute × η_CPU) × PUE_adjust × utilization_rate
Où :
P_GPU = puissance nominale du GPU en watts (TDP ou puissance mesurée)
P_CPU = puissance du CPU système en watts
t_compute = temps de calcul en heures
η_GPU, η_CPU = taux d'utilisation réelle des ressources (typiquement 60-80% pour GPU, 20-30% pour CPU)
PUE = Power Usage Effectiveness du data center utilisé
utilization_rate = taux d'utilisation du serveur (pourcentage du temps où le GPU exécute une inférence)
Analyse unitaire de notre calcul :
Analyse = [(token / (token/s)) + (token / (token/s))] x [(Watt x sans_unité) + (Watt x sans_unité)] x sans_unité
Analyse = [secondes + secondes] x [Watt + Watt] x sans_unité
Analyse = [secondes] x [Watt] x sans_unité
Analyse = Watt x secondes = Joules
9.4.4 Estimation du Temps de Calcul (t_compute)
Le temps de calcul peut être estimé en fonction du nombre de tokens et du débit du modèle. Pour calculer cette information de temps, on pose le cas de la full self-attention (matrice d'attention calculée entièrement) sans prendre en compte les nouvelles techniques comme la sparse attention, la flash attention ou même la linear attention. On se place dans le « pire cas » y compris dans l'utilisation des modèles les plus récents.
t_compute_prefill = (input_tokens^2 / (throughput/ 3600)) t_compute_decode = (output_tokens / (throughput/ 3600))
Où les débits (throughput) sont exprimés en tokens par seconde et le temps en heures.
9.5 Données de Base des Fournisseurs de Modèles
9.5.1 OpenAI (ChatGPT / GPT-5)
OpenAI ne divulgue pas les chiffres énergétiques officiels, mais publie sa tarification de l'API basée sur les tokens. Selon le site officiel des prix d'OpenAI (octobre 2025)[20] :
GPT-5 : Input $1.25 / 1M tokens, Output $10.00 / 1M tokens
GPT-4.1 : Input $2.00 / 1M tokens, Output $8.00 / 1M tokens
Pour l'énergie, les estimations académiques basées sur le benchmarking direct fournissent des données plus utiles. Selon l'étude d'énergie de ChatGPT publiée en février 2025 par Epoch.ai : « We find that typical ChatGPT queries using GPT-4o likely consume roughly 0.3 watt-hours, which is ten times less than the older estimate »[21]. Cette source note également : « According to prices compiled by Artificial Analysis, Llama 3.1 405B costs $3.50 per million output tokens on average, which is more than 10 times more expensive. The cost of renting GPUs is almost certainly the biggest cost of running these APIs, so this suggests that providers need about 10x as many GPUs compared to if they achieved 100% utilization. This means utilization is roughly 10%, increasing the GPUs required, and hence our energy estimate, by 10x »[22].
Cette observation est cruciale : l'utilisation réelle des GPU pour les services d'API cloud est estimée à seulement 10%, ce qui signifie que 90% de la puissance est consommée par des serveurs en attente ou exécutant d'autres tâches. Cela justifie l'ajustement utilization_rate dans notre formule.
Pour GPT-5 spécifiquement, les estimations indépendantes indiquent une consommation beaucoup plus élevée que GPT-4o. Selon l'étude de l'Université de Rhode Island publiée en août 2025 : « Independent research by the University of Rhode Island's AI lab estimates GPT-5 uses approximately 8.6× more energy per query than GPT-4, consuming around 18.35 watt-hours on average, and peaking up to 40 Wh per medium-length response »[23].
9.5.2 Azure (Microsoft)
Microsoft Azure n'expose pas non plus de données énergétiques directes. Cependant, Microsoft a publié plusieurs articles sur la durabilité des datacenters en décembre 2024 et septembre 2024. Le document « Sustainable by design: Innovating for energy efficiency in AI, part 1 » indique : « We use the power of software to drive energy efficiency at every level of the infrastructure stack, from datacenters to servers to silicon »[24]. Microsoft revendique des taux d'utilisation de « 80 to 90% utilization at scale »[25] grâce à Project Forge, son système d'ordonnancement basé sur l'IA.
L'étude benchmarking énergétique de 2025 effectue des mesures directes sur les instances Azure avec des GPU H100. Les résultats montrent que les coûts énergétiques d'Azure sont comparables à OpenAI, avec quelques variations selon la configuration[26].
9.5.3 DeepL (Traduction)
DeepL, basée en Allemagne, a établi des data centers en Islande pour minimiser son impact carbone. Selon son blog de durabilité (décembre 2025) : « DeepL is building a greenhouse gas (GHG) inventory to measure emissions across our operations and value chain. By tracking emissions throughout the business and setting future targets, we take meaningful steps to reduce our environmental impact »[27].
Cependant, DeepL ne publie pas de chiffres précis d'énergie par token. Un article de recherche comparative de 2025 sur la traduction et l'impact environnemental rapporte : « The fine-tuned Gemma-3-4B model achieved performance comparable to GPT-4o and outperformed GPT-4o-mini across all metrics, while consuming approximately 15 times less energy per inference »[28]. Cela suggère que les modèles de traduction spécialisés peuvent être considérablement plus efficaces que les LLM généraux pour la traduction.
9.5.4 Intento
Intento ne divulgue pas de données énergétiques publiques. Intento opère comme un agrégateur de services MT/IA, routant les requêtes vers divers fournisseurs (OpenAI, Google, DeepL, Azure, etc.). Par conséquent, la consommation énergétique d'Intento dépend entièrement des fournisseurs sous-jacents plus un léger surcoût pour la routage et l'orchestration.
Cas 1 — Utilisation d'un fournisseur unique via Intento
Lorsque le client utilise Intento avec un seul provider explicitement configuré, la consommation énergétique associée à Intento est assimilée à celle du fournisseur sous-jacent. Dans ce cas :
Intento joue un rôle de pass-through (orchestration légère)
La consommation énergétique est estimée comme si le client appelait directement le fournisseur
Formellement : E_Intento ≈ E_provider
Cas 2 — Utilisation du Smart Routing (distribution probabiliste)
Lorsque le client utilise la fonctionnalité de Smart Routing d'Intento, les requêtes sont distribuées dynamiquement entre plusieurs fournisseurs selon des critères tels que :
le coût
la qualité de sortie
la disponibilité
ou potentiellement, à terme, l'empreinte carbone
Dans ce cas, la consommation énergétique doit être modélisée comme une espérance pondérée sur l'ensemble des fournisseurs utilisés.
Modélisation probabiliste
Soit un ensemble de fournisseurs : {P1, P2, …, Pn}
Chaque fournisseur Pi est sélectionné avec une probabilité wi, telle que : ∑wi = 1
La consommation énergétique moyenne par requête est alors donnée par :
E_Intento = ∑(wi × E_Pi)
Où :
E_Pi est la consommation énergétique estimée du fournisseur Pi pour une requête donnée (calculée selon la méthodologie décrite dans les sections précédentes)
wi est la probabilité de routage vers ce fournisseur
9.6 Mix Énergétique et PUE par Pays
9.6.1 Intensité Carbone de l'Électricité
Le calcul complet de l'impact carbone nécessite de connaître la source d'énergie du data center. Selon l'Agence Européenne de l'Environnement (novembre 2024)[29] :
Islande : ~5 gCO₂e/kWh (presque 100% énergie renouvelable)
Norvège : 30 gCO₂e/kWh (hydroélectricité abondante)
France : ~60 gCO₂e/kWh (mix nucléaire et renouvelable)
Allemagne : ~140 gCO₂e/kWh (transition énergétique en cours, part croissante de renouvelables)
Pays-Bas : ~200 gCO₂e/kWh (mix diverse)
États-Unis (moyenne) : 380-400 gCO₂e/kWh (dépend fortement de l'état)
Moyenne mondiale : 481 gCO₂e/kWh[30]
DeepL opérant principalement en Islande et Allemagne, on peut estimer une intensité carbone moyenne de (5 + 140)/2 = 72.5 gCO₂e/kWh pour DeepL.
OpenAI et Azure opèrent dans plusieurs régions, incluant les États-Unis (mix régional ~370-400 gCO₂e/kWh) et des régions avec plus de renouvelables. Une moyenne pondérée par déploiement suggère ~250-300 gCO₂e/kWh.
9.6.2 Power Usage Effectiveness (PUE) par Région
Selon Mordor Intelligence (août 2025), « Germany's Energy Efficiency Act will prohibit data centers above 1.2 PUE beginning 2027»[31]. Cette régulation sera effectivement plus stricte que la moyenne mondiale.
Allemagne (standard nouveau) : PUE 1.2-1.25 (cible réglementaire)
Islande (DeepL) : PUE 1.1-1.15 (data centers hautement optimisés)
États-Unis (hyperscale) : PUE 1.2-1.4 (entreprises comme Google et Meta atteignent 1.09-1.12, mais moyenne plus haute)
Moyenne mondiale 2024 : PUE 1.56[32]
Facilities les plus efficaces : PUE 1.1 (Google rapporte 1.09)[33]
Pour les calculs, nous utiliserons : DeepL = 1.15, OpenAI/Azure = 1.3 (moyenne pondérée des US data centers), Moyenne mondiale = 1.56.
9.7 Hardware et Puissance
9.7.1 Consommation Énergétique du GPU
Les GPUs utilisés pour l'inférence LLM varient considérablement. Les plus courants sont :
NVIDIA A100 : TDP 250W, puissance opérationnelle typique ~180-200W à 70% d'utilisation
NVIDIA H100 : TDP 700W, puissance opérationnelle typique ~500-550W à 70% d'utilisation
NVIDIA H200 : TDP 700W, performances améliorées mais consommation similaire
Lors d'une inférence LLM, on distingue généralement deux phases :
Pour la phase de prefill (traitement des inputs), la charge GPU est élevée mais la latence est importante
Pour la phase de decode (génération), la charge GPU est plus faible (chaque GPU génère un token à la fois) mais la latence est critique
Selon l'étude Infrastructure-aware benchmarking de 2025 : « An A100 can generate up to 72000 tokens per hour, 400W for the A100, 70W for the CPU, and PUE = 1.1, 26 Joules of W consumption per generated token »[34]. Ce chiffre de 26 joules par token décodé (output token) pour une A100 est une référence directe très utile.
Conversion : 26 joules = 26 / 3,600,000 kWh = 0.0000072 kWh/token ≈ 7.2 microWh/token pour la génération avec A100 et PUE=1.1.
Pour les H100 (environ 3-4 fois plus puissants mais 3-4 fois plus puissants en consommation), on peut estimer ~24 microWh/token pour le décodage et ~ 216000 tokens par heure.
Il est important de souligner que ces chiffres constituent des ordres de grandeur issus de benchmarks académiques, et non des valeurs fixes ou contractuelles. Le domaine de l'inférence LLM est en forte évolution, avec des gains rapides en performance énergétique. À titre illustratif, NVIDIA met en avant des améliorations significatives de l'efficacité énergétique avec ses nouvelles architectures B200, notamment lorsqu'elles sont combinées à des modèles ouverts optimisés comme Mistral. Ces avancées montrent que, à qualité équivalente, l'énergie consommée par token peut être fortement réduite grâce à des architectures GPU plus efficientes, des optimisations mémoire et des modèles mieux adaptés à la tâche[35].
Google n'est pas en reste et propose une approche différente avec ses propres puces, les TPUs. Leur dernière version, «Trillium », est conçue spécifiquement pour l'IA et réussit à être 67% plus économe en énergie que la précédente[36]. En plus du matériel, Google a optimisé son logiciel « JetStream » pour que des modèles comme Mixtral fonctionnent trois fois plus vite, ce qui réduit mécaniquement la facture électrique pour chaque mot généré[37].
9.7.2 Puissance CPU et Overhead Système
Selon le papier HotCarbon de 2024 sur le cycle de vie des LLM : « While specialized AI engines account for the lion's share of power consumption in generative AI, general purpose CPUs incur non-trivial embodied carbon overheads »[38]. Le CPU système consomme typiquement 70-100W pour un serveur de datacenter, soit environ 15-30% de la consommation totale du GPU + CPU.
9.8 Formules de Calcul de l'Énergie due à l'Infrastructure Réseau
L'exclusion de la consommation réseau dans le calcul de l'empreinte énergétique d'une requête IA s'explique principalement par la nature non déterministe et mutualisée d'Internet, qui rend toute estimation précise extrêmement complexe voire impossible à l'échelle d'une simple interaction. Contrairement à un GPU dont on peut mesurer la consommation exacte pendant les millisecondes d'une inférence, le transport de la donnée traverse une multitude de routeurs et de câbles (souvent transfrontaliers) dont l'infrastructure est allumée en permanence, qu'il y ait du trafic ou non. Attribuer une part de cette consommation « fixe » à une requête unique relève de l'arbitraire, d'autant que le chemin parcouru change dynamiquement et que l'intensité carbone de l'électricité varie à chaque frontière traversée. De plus, pour les modèles de langage (LLM), l'énergie nécessaire au calcul (inférence sur des puces H100/A100) est souvent plusieurs ordres de grandeur supérieure à celle du transport de quelques kilooctets de texte, rendant la part du réseau statistiquement négligeable dans le bilan final.
Pourquoi le réseau est souvent exclu des calculs
La difficulté méthodologique majeure réside dans l'absence de proportionnalité énergétique des équipements réseau : un routeur consomme presque autant d'énergie à vide qu'à pleine charge. Isoler le coût marginal d'une requête individuelle nécessite donc des hypothèses de modélisation lourdes (diviser la conso totale par le volume de données mondial) qui ne reflètent pas la réalité physique instantanée.
L'infrastructure est une « boîte noire » : Il est impossible de savoir si votre requête vers un serveur aux USA est passée par un câble sous-marin spécifique ou a été routée via Londres ou Paris, empêchant l'application d'un mix électrique national précis.
La volatilité temporelle : La consommation réelle dépend de la congestion du réseau à la milliseconde près (heure de pointe vs nuit), une donnée inaccessible pour l'utilisateur final de l'API.
Le ratio Signal/Calcul : Dans l'IA générative, on envoie très peu de données (un « prompt » textuel) pour déclencher un calcul massif. Contrairement au streaming vidéo (beaucoup de données, peu de calcul), ici le coût énergétique est concentré dans le datacenter, rendant l'approximation « Réseau = 0 » acceptable pour simplifier l'analyse.
9.9 Formules de Calcul par Profil d'Utilisation
9.9.1 Profil 1 : Traduction (TRANSLATION)
Caractéristiques :
Input : contenu du topic (topic_size)
Output : contenu traduit (≈topic_size, car la traduction ne change pas drastiquement la longueur)
Exemple : DeepL ou système de traduction spécialisé
Calcul des tokens :
tokens_input = topic_size / 4 (ou len(enc.encode(text)) d'après tiktoken pour les modèles OpenAI)
Lorsque le texte est disponible (ex. échantillonnage interne, logs de contenu accessibles), nous calculons le nombre de tokens exact à l'aide du tokenizeur BPE tiktoken d'OpenAI, en utilisant l'encodage correspondant au modèle (encoding_for_model). Cela permet de capturer la tokenisation réelle (non-linéaire) et d'éviter une hypothèse fixe caractères/token.
Plus simplement, pour évaluer le volume de texte (en « tokens »), nous utilisons deux approches selon les données disponibles. Si nous avons accès au texte lui-même et au modèle utilisé (cas général du projet), nous utilisons l'outil de calcul précis d'OpenAI pour obtenir le chiffre exact. En revanche, si nous ne connaissons que le nombre de caractères, nous appliquons une estimation simple et reconnue : un token équivaut environ à 4 caractères pour l'explication théorique.
Lorsque le texte n'est pas disponible et que seules des métriques agrégées (ex. topic_size en caractères) sont accessibles, nous utilisons une approximation cohérente avec l'anglais, langue majoritaire chez Fluid Topics : 1 token ≈ 4 caractères.
tokens_output = topic_size / 4
Paramètres énergétiques :
PUE_deepl = PUE_islande = 1.15
η_CPU = 30-15% selon HotCarbon
η_CPU + η_GPU = 1 car on se place dans le pire cas de consommation (Réseau Dense pas MoE)
utilization_rate = 1 car chaque requête doit porter le « reste à gagner » de l'utilization_rate
Formule d'énergie :
E_translation = E_training + E_inference + E_infra
E_translation = ~0 + E_inference + ~0
E_translation = (P_GPU × t_compute × η_GPU + P_CPU × t_compute × η_CPU) × PUE × utilization_rate
E_translation = t_compute × (P_GPU × η_GPU + P_CPU × η_CPU) × PUE_islande × 1
E_translation = (t_compute_prefill + t_compute_decode) × [(700 × (1-(30+15)/200)) + (100+70)/2 × (30+15)/200] × 1.15
E_translation = ((input_tokens^2 / (throughput/ 3600)) + (output_tokens / (throughput/ 3600))) × [(700 × (1-(30+15)/200)) + (100+70)/2 × (30+15)/200] × 1.15
E_translation_per_token = ((input_tokens^2 / (216000 / 3600)) + (output_tokens / (216000 / 3600))) × [(700 × (1-(30+15)/200)) + (100+70)/2 × (30+15)/200] × 1.15
E_translation = ((input_tokens^2 / 60) + (output_tokens / 60)) x [(700 x (1 - 0.225)) + (85 x 0.225)] x 1.15
E_translation = ((input_tokens^2 + output_tokens) / 60) x [542.5 + 19.125] x 1.15
E_translation = ((input_tokens^2 + output_tokens) / 60) x 561.625 x 1.15
E_translation = ((input_tokens^2 + output_tokens) / 60) x 645.87
E_translation = (input_tokens^2 + output_tokens) x 10.7645
9.9.2 Profil 2 : Chatbot (CHATBOT)
Caractéristiques :
Input : n topics (1 à 50) + prompt systemchatbot
Output : réponse générée (200-400 caractères typiquement, soit ~57-114 tokens)
Exemple : GPT-4o ou équivalent (cas général) ou GPT-5.x (cas optimisé récent)
Calcul des tokens :
tokens_input = (sum_all(topic_sizes) + prompt_size) / 4
tokens_output ≈ 300 tokens (moyenne 200-400 caractères)
Paramètres énergétiques :
PUE_gpt = PUE_us = 1.3
η_CPU = 30-15% selon HotCarbon
η_CPU + η_GPU = 1 car on se place dans le pire cas de consommation (Réseau Dense pas MoE)
utilization_rate = 1 car chaque requête doit porter le « reste à gagner » de l'utilization_rate
Formule d'énergie :
E_chatbot = E_training + E_inference + E_infra
E_chatbot = ~0 + E_inference + ~0
E_chatbot = (P_GPU × t_compute × η_GPU + P_CPU × t_compute × η_CPU) × PUE × utilization_rate
E_chatbot = ((input_tokens^2 / (216000 / 3600)) + (output_tokens / (216000 / 3600))) × (700 × (1-0.225) + 85 × 0.225) × 1.3 × 1
E_chatbot = ((((sum_all(topic_sizes) + prompt_size) / 3.5)^2 / (216000 / 3600)) + (300 / (216000 / 3600))) × (700 × (1-2.225) + 85 × 0.225) × 1.3 × 1
E_chatbot = (((sum_all(topic_sizes) + prompt_size) / 4)^2 / 60) + 3650.5625
9.9.3 Profil 3 : Génération / Completion (COMPLETION)
Caractéristiques :
Input : 1 topic + prompt
Output : contenu généré (200-400 caractères)
Modèle : GPT-4o ou GPT-5.x
Calcul des tokens :
tokens_input = (topic_size + prompt_size) / 4
tokens_output ≈ 300 tokens (moyenne 200-400 caractères)
Paramètres énergétiques :
PUE_chatpgt = PUE_us = 1.3
η_CPU = 30-15% selon HotCarbon
η_CPU + η_GPU = 1 car on se place dans le pire cas de consommation (Réseau Dense pas MoE)
utilization_rate = 1 car chaque requête doit porter le « reste à gagner » de l'utilization_rate
Formule d'énergie :
E_completion = E_training + E_inference + E_infra
E_completion = ~0 + E_inference + ~0
E_completion = (P_GPU × t_compute × η_GPU + P_CPU × t_compute × η_CPU) × PUE × utilization_rate
E_completion = ((topic_size + prompt_size) / 4)^2 / 60) + 3650.5625
9.10 Différences Entre les Profils et Justifications
9.10.1 Traduction vs. Génération / Chatbot
La traduction est 15 à 50 fois plus efficace énergétiquement que la génération de contenu avec un LLM généraliste. Selon l'étude comparative de 2025 : « The fine-tuned Gemma-3-4B model achieved performance comparable to GPT-4o and outperformed GPT-4o-mini across all metrics, while consuming approximately 15 times less energy per inference »[39].
Raisons scientifiques :
Tâche discriminative vs. générative : Selon le papier « Watts Driving the Cost of AI Deployment? » (2024), « Generative tasks are more energy- and carbon-intensive compared to discriminative tasks »[40]. La traduction, en tant que tâche plus structurée avec une espace de sortie plus restreinte (vocabulaire traduit), est énergétiquement plus efficace que la génération libre générale.
Taille et spécialisation du modèle : Les modèles de traduction dédiés (7B à 13B paramètres) surpassent les LLM généraux de 175B+ paramètres pour la tâche de traduction. La recherche montre que l'utilisation du modèle approprié pour la tâche (scaling law) réduit la consommation de 27.8% en moyenne[41].
Architectures optimisées : Les systèmes MT modernes utilisent des techniques comme la quantification, Mixture of Experts (MoE), et Flash Attention, réduisant la consommation d'énergie de 85% selon les sources sectorielles[42].
9.10.2 Chatbot vs. Completion
Le chatbot traite plusieurs topics en input (jusqu'à 50) tandis que completion n'en traite qu'un. De plus, le chatbot maintient une session et peut faire plusieurs tours, accumulant les coûts.
Différences clés :
Longueur d'input : Pour n=50 topics, tokens_input peut atteindre 18,750 tokens, soit 9x plus qu'une completion (625 tokens). Le coût de prefill croît quadratiquement[43], donc le coût d'input du chatbot est ~20-30x supérieur.
Nombre d'inférences : Une conversation chatbot implique généralement plusieurs tours (turn-taking), tandis que completion est généralement single-turn.
Latence requise : Le chatbot nécessite une latence faible pour une bonne UX conversationnelle, ce qui peut nécessiter des configurations GPU sous-utilisées (réservation de capacité).
9.11 Données Spécifiques des Fournisseurs (Résumé)
9.11.1 OpenAI (GPT-5 / GPT-4o)
Localisation : États-Unis (multiple régions), quelques data centers en Europe
Intensité carbone : ~300 gCO₂e/kWh (moyenne pondérée US/EU)
PUE : ~1.3 (estimation basée sur l'utilisation 10% rapportée)
Consommation par requête :
GPT-4o (requête moyenne ~3000 tokens) : 0.3 Wh = 0.3 × 10⁻³ kWh
GPT-5 (requête moyenne ~3000 tokens) : 18.35 Wh (estimation indépendante) = 18.35 × 10⁻³ kWh
Ratio énergétique : GPT-5 consomme ~61× plus d'énergie que GPT-4o par requête, malgré une meilleure qualité.
9.11.2 Azure
Localisation : États-Unis, Europe, autres régions
Intensité carbone : ~280 gCO₂e/kWh (mix régional avec priorité aux renouvelables)
PUE : ~1.25 (Microsoft revendique 80-90% d'utilisation via Project Forge[44])
Consommation par requête : Comparable à OpenAI pour modèles similaires, avec variations liées à la configuration régionale
9.11.3 DeepL
Localisation : Islande + Allemagne
Intensité carbone : ~72.5 gCO₂e/kWh (très bas grâce à l'Islande)
PUE : ~1.15 (data centers d'Islande très efficaces)
Consommation par requête :
Traduction (DeepL propriétaire) : 0.0005-0.002 Wh = 0.5-2 microWh (estimation basée sur 15x plus efficace que GPT-4o pour MT)
Avantage carbone : Même avec une consommation énergétique 10x plus faible (per task), l'intensité carbone extrêmement faible de l'Islande (5 gCO₂/kWh) fait que DeepL produit ~7-10x moins de CO₂ qu'OpenAI pour une traduction équivalente.
9.11.4 Intento
Localisation : Dépend du routage (peut être n'importe quel fournisseur)
PUE / Intensité carbone : Agrégat pondéré de tous les fournisseurs backend
Surcoût : +5-15% d'énergie/latence pour orchestration et routage
10. Outils de Mesure en Production
La mesure de la consommation énergétique des LLM en production est essentielle pour valider les estimations théoriques et affiner continuellement la méthodologie. Plusieurs outils et frameworks existent pour cette fin.
10.1 ETHIC AI
Une ressource pertinente sur la mesure de la consommation énergétique des systèmes d'IA en production est le rapport « Calculating AI's Energy Use » publié par EthicAI. Ce document propose une méthodologie détaillée pour évaluer objectivement l'énergie utilisée par des modèles d'IA dans des contextes réels, en intégrant des éléments tels que les charges GPU effectives, l'efficacité des infrastructures (PUE), et la variabilité des data centers. Il complète les outils existants comme CodeCarbon et Electricity Maps en fournissant un cadre d'analyse pour relier des mesures empiriques à des estimations globales, ce qui est utile pour valider et contextualiser les estimations de consommation énergétique dans notre méthodologie[45].
10.2 CodeCarbon
CodeCarbon est une bibliothèque Python open-source qui suit la consommation électrique et les émissions de carbone pendant l'exécution du code. La bibliothèque dispose de plusieurs avantages notables. L'intégration est facile avec du code Python existant. Le suivi en temps réel de la consommation d'électricité est possible. Elle utilise des données d'intensité carbone par région issues de l'API Electricity Maps. Enfin, aucune dépendance matérielle externe n'est requise pour le fonctionnement basique.
Cependant, CodeCarbon présente aussi des inconvénients. Les mesures peuvent être imprécises si le processus n'est pas la charge dominante du système. Elles dépendent de la précision des drivers GPU pour mesurer la consommation réelle (PyNVML pour NVIDIA), bien que cela concerne les fournisseurs et non Fluid Topics qui ne possède pas ses propres GPUs. Elle n'inclut pas naturellement le PUE du data center sauf si configuré manuellement. Enfin, elle est limitée aux exécutions locales ou à SSH, sans API cloud native[46].
Les limites principales sont que CodeCarbon mesure le GPU directement mais pas l'infrastructure globale. Selon le papier « How Hungry is AI », beaucoup des calculs actuels de consommation énergétique IA ne tiennent compte que de la consommation active des machines, passant sous silence plusieurs facteurs critiques. De ce fait, ils représentent l'efficacité théorique plutôt que l'efficacité opérationnelle réelle à grande échelle. CodeCarbon par défaut ne mesure que la consommation active du GPU[47].
10.3 Green Algorithms Initiative
La Green Algorithms Initiative fournit une calculatrice en ligne basée sur des formules empiriques publiées. Elle prend en compte le type de processeur et sa puissance, la région du data center et son intensité carbone, le PUE estimé, et la durée d'exécution.
Avantages : La calculatrice est simple et accessible sans intégration de code. Elle ajuste automatiquement pour PUE et régions.
Inconvénients : L'interface est web et ne dispose pas d'API pour l'automatisation. Les estimations sont moins précises que CodeCarbon car pas de mesure réelle du GPU. Elle nécessite l'entrée manuelle des paramètres.
10.4 Electricity Maps API
Electricity Maps (anciennement WattTime) fournit une API pour l'intensité carbone en temps réel par région. Plusieurs publications l'utilisent.
Avantages : Elle fournit des données de carbone en temps réel par région géographique. Elle peut être combinée avec CodeCarbon. L'API est publique et bien documentée. Elle est utile pour l'optimisation temporelle et spatiale des workloads.
Inconvénients : Elle nécessite une clé API (tier gratuit limité). Elle demande de connaître la localisation du data center. Elle n'inclut pas automatiquement la mesure de l'énergie (doit être couplée à CodeCarbon ou autre).
10.5 Google Sustainable AI Initiative Framework
Google a publié en août 2025 une méthodologie complète pour mesurer l'énergie, les émissions et l'impact hydrique des requêtes Gemini. Cette approche mesure l'énergie active du serveur (TPU/GPU), l'infrastructure data center (incluant refroidissement), le matériel système (CPU, DRAM, stockage), et l'utilisation de l'eau (souvent oubliée, environ 0.12 millilitres d'eau par requête médiane Gemini)[48].
Avantages : La méthodologie est complète et peer-reviewed. Elle inclut infrastructure et overhead. Elle rend compte de l'inefficacité réelle (non théorique).
Inconvénients : Elle est spécifique à l'écosystème Google (TPU, infrastructure interne). Elle n'est pas facilement transférable à d'autres fournisseurs/hardware. Elle requiert accès à des données internes non disponibles pour les clients cloud externes.
11. Implémentation Pratique et Avantages Commerciaux
11.1 Implémentation Proposée
La méthodologie peut être implémentée via un script Python utilisant les données collectées par Fluid Topics (via ses analytics) et les facteurs énergétiques détaillés dans cette documentation. Une implémentation complète incluerait l'intégration de l'API Electricity Maps pour obtenir l'intensité carbone réelle par région et l'intégration optionnelle de CodeCarbon pour valider les estimations lors de tests.
11.2 Avantages pour Fluid Topics
Pour la plateforme elle-même :
Estimation précise et par-client de la consommation énergétique
Estimation par type d'usage IA (traduction vs chatbot vs complétion)
Comparaison claire des efficacités énergétiques entre profils
Possibilité d'optimiser les modèles et prompts pour réduire la consommation
Pour les clients et la valeur commerciale :
Transparence directe : « Voici exactement combien l'IA/MT consomme pour votre portail / vos usages »
Comparabilité : Suivi dans le temps (avant/après une fonctionnalité, un changement de modèle)
Pilotage : Fixer des budgets énergétiques, de tokens, ou de carbone par équipe ou par cas d'usage
Argument de vente majeur : Pour les entreprises sensibles aux directives CSRD/ESG, cette transparence est un différenciatif clé
Différenciation concurrentielle : Versus des concurrents « boîte noire » qui refusent de publier ces métriques
Intégration aux appels d'offres : Ces métriques deviennent des critères d'évaluation dans les processus d'approvisionnement en IT
En interne pour Fluid Topics :
Création d'un dashboard montrant le pourcentage de personnes consultants qui bénéficient des services IA
Réflexion approfondie sur le sens que les travailleurs donnent à leur travail (impact social interne) liée à ces enjeux de durabilité
Positionnement de la plateforme comme leader en matière de responsabilité environnementale dans le secteur de la gestion documentaire
12. Recommandations Futures et Limitations
12.1 Validation de l'Énergie par Token pour les Fournisseurs
L'estimation de l'énergie par token pour DeepL, OpenAI et Azure mérite validation indépendante via des benchmarks directs et des contacts directs avec les fournisseurs, notamment pour GPT-5 où les données sont très récentes.
12.2 Conversion Token-Caractères pour Langues Européennes
La question de savoir si utiliser la conversion anglaise (1 token = 4 caractères) ou une conversion pour les langues européennes (1 token ≈ 3.5 caractères) nécessite une étude détaillée étant donné la base utilisateur internationale de Fluid Topics.
12.3 Optimisation des Tokens et Routage Intelligent
Plusieurs pistes d'optimisation doivent être explorées : diminution des tokens en entrée et en sortie via des techniques de prompt engineering, routage dynamique vers des modèles moins énergétiques selon la tâche, et utilisation de modèles open-source plus efficaces quand cela est possible.
12.4 Configuration des Data Centers par Fournisseur
Chaque fournisseur utilise des clouds répartis dans plusieurs pays. L'approche actuelle utilise les moyennes du pays où les fournisseurs ont majoritairement leurs data centers. Une estimation plus fine pourrait permettre au client de choisir la région et d'inclure ce choix dans le résultat final.
12.5 Données Fictives pour Testing
La création d'un ensemble de données fictives mais réalistes faciliterait le testing et la validation de la méthodologie avant déploiement en production.
12.6 Format d'Intégration
Une clarification du format optimal pour intégrer ce projet dans les processus existants de Fluid Topics (APIs, webhooks, dashboards, exports) est nécessaire.
13. Conclusion
Cette méthodologie complète fournit à Fluid Topics un framework robuste pour quantifier, documenter et communiquer l'impact énergétique et carbone de ses services IA. Appuyée sur des données scientifiques et des déclarations officielles de fournisseurs, elle reconnaît les limitations inhérentes à toute estimation cloud en contexte réel, et propose des hypothèses justifiées et documentées pour les paramètres où les données précises ne sont pas disponibles.
L'adoption de cette méthodologie positionne Fluid Topics comme leader en matière de transparence et de responsabilité environnementale, offrant une valeur commerciale immédiate aux clients soumis à la directive CSRD et une différenciation claire versus la concurrence. Internement, elle offre des leviers pour optimiser et piloter l'impact environnemental de la plateforme, contribuant ainsi à une IA plus durable et responsable.
Références
[1] Directive (UE) 2022/2464 du Parlement européen et du Conseil – CSRD. https://eur-lex.europa.eu/eli/dir/2022/2464/oj
[2] Commission européenne – Finance durable & ESG. https://finance.ec.europa.eu/sustainable-finance_en ; OCDE – ESG et performance extra-financière. https://www.oecd.org/finance/esg-investing.htm
[3] Fluid Topics – Documentation système
[4] OpenAI – tiktoken tokenizer. https://github.com/openai/tiktoken
[5] Mielke et al., Between Words and Characters: A Brief History of Open-Vocabulary Modeling. https://www.semanticscholar.org/paper/Between-words-and-characters%3A-A-Brief-History-of-in-Mielke-Alyafeai/d617f51833860dc50d202af7f80be71304b2e994
[6] MIT News, « Explained: Generative AI's environmental impact », janvier 2025. https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117
[7] How Hungry is AI? Benchmarking Energy, Water, and Environmental Impact of LLM Inference Across 30 Model Systems, 2025. arxiv.org/html/2505.09598v1
[8] Statista, « Data center average annual PUE worldwide 2024 », avril 2025
[9] WEF Forum, « How data centres can avoid doubling their energy use », décembre 2025. https://www.weforum.org/stories/2025/12/data-centres-and-energy-demand/
[10] data4group – Dictionnaire du datacenter. https://www.data4group.com/dictionnaire-du-datacenter/qu-est-ce-qu-un-pue/
[11] Google Cloud Blog, « Measuring the environmental impact of AI inference », août 2025. https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference/
[12] How Hungry is AI? op. cit. https://arxiv.org/pdf/2505.09598
[13] OpenAI Help Center, « What are tokens and how to count them? », septembre 2025. https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
[14] Epoch.ai, « How much energy does ChatGPT use? », février 2025. https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
[15] Inference.net, « Optimizing Latency vs. Response Time in AI Deployment », mai 2025
[16] OpenRouter. https://openrouter.ai/google/gemini-3-flash-preview/performance ; llmperf. https://github.com/ray-project/llmperf ; Hugging Face. https://huggingface.co/spaces/optimum/llm-perf-leaderboard
[17] Papineni et al., « Watts Driving the Cost of AI Deployment? », 2024. arxiv.org/html/2311.16863v3
[18] MIT News, op. cit.
[19] Epoch.ai, op. cit.
[20] OpenAI Pricing. https://openai.com/api/pricing/, octobre 2025
[21] Epoch.ai, op. cit.
[22] Epoch.ai, op. cit.
[23] "GPT-5 Energy Efficiency vs GPT-4: AI's Green Leap Forward", août 2025, https://aiinsighttalks.com/gpt-5-energy-efficiency-vs-gpt-4-ais-green-leap-forward/
[24] Microsoft Cloud Blog, "Sustainable by design: Innovating for energy efficiency in AI, part 1", septembre 2024
[25] Ibid.
[26] How Hungry is AI? op. cit.
[27] DeepL Sustainability, "Harnessing AI the sustainable way", décembre 2025, https://www.deepl.com/en/sustainability/environment
[28] Castaldo et al., "Balancing Translation Quality and Environmental Impact", 2025, ceur-ws.org/Vol-4112/19_main_long.pdf
[29] EEA, "Greenhouse gas emission intensity of electricity generation in Europe", novembre 2025
[30] Statista, "Power sector carbon intensity worldwide by country 2023", juillet 2024
[31] Mordor Intelligence, "Europe Data Center Power Market Size & Share Analysis", août 2025
[32] Statista, op. cit.
[33] WEF Forum, op. cit.
[34]  Infrastructure-aware benchmarking paper, 2024, https://archives.iw3c2.org/www2022/wp-content/uploads/Sponsors/WWW2022-Technology-Innovation-Institute.pdf
[35] NVIDIA – Blog développeur, architectures B200. https://developer.nvidia.com/blog/nvidia-accelerated-mistral-3-open-models-deliver-efficiency-accuracy-at-any-scale/
[36] Google Cloud Blog – Introducing Trillium 6th-gen TPUs. https://cloud.google.com/blog/products/compute/introducing-trillium-6th-gen-tpus
[37] Google Cloud Blog – AI Hypercomputer Inference Updates. https://cloud.google.com/blog/products/compute/ai-hypercomputer-inference-updates-for-google-cloud-tpu-and-gpu
[38]  "Towards Carbon-efficient LLM Life Cycle", HotCarbon 2024, https://hotcarbon.org/assets/2024/pdf/hotcarbon24-final154.pdf
[39] Castaldo et al., op. cit.
[40] Papineni et al., op. cit.
[41] "Reducing the World AI Energy Consumption Through Model Selection and Scaling", 2024, arxiv.org/html/2510.01889v1
[42] DeepL Bridges, "Green AI in Translation: Why DeepL's Efficiency Matters More Than Ever", novembre 2025
[43] Epoch.ai, op. cit.
[44] Microsoft Cloud Blog, op. cit
[45] EthicAI – « Calculating AI's Energy Use »
[46] Documentation CodeCarbon https://codecarbon.io/
[47] Papier « How Hungry is AI »
[48] Google Sustainable AI Initiative Framework – août 2025

