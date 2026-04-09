from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse

import pathlib
import uuid
import shutil

app = FastAPI()

@app.post("/api/v1/upscale", response_class=FileResponse)
async def upscale(file: UploadFile):
    content = await file.read()
    path = pathlib.Path(f"images/{uuid.uuid4().hex}")
    # /images 폴더 없으면 오류나서 parents=True 추가
    path.mkdir(parents=True)
    source = path / file.filename
    with open(source, "wb") as f: f.write(content)
    target = path / f"{source.stem}_upscaled{source.suffix}"
    shutil.copy(source, target)
    return FileResponse(target, filename=target.name)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4398)
