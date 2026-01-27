from fastapi import FastAPI, Query, UploadFile, File, HTTPException
import yaml
from interface import run_from_analytics

app = FastAPI(
    title="Energy & Carbon Calculator API",
    description="API de calcul de consommation énergétique et carbone (gCO₂e)",
    version="1.0"
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/energy")
async def compute_energy(
    region: str = Query(default=None, description="Région de calcul (france, usa, germany, iceland)"),
    analytics_file: UploadFile = File(..., description="Fichier YAML des analytics")
):
    try:
        content = await analytics_file.read()
        analytics = yaml.safe_load(content)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Fichier YAML invalide: {exc}")

    if not isinstance(analytics, dict):
        raise HTTPException(status_code=400, detail="Le contenu YAML doit être un dictionnaire à la racine.")

    return run_from_analytics(analytics=analytics, region=region)
