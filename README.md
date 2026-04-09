# Upscaling API (Mock)

업스케일링 API 스펙을 맞춰두기 위한 임시 서버입니다. 실제 업스케일링 없이 원본 파일을 그대로 반환합니다.

## API

`POST /api/v1/upscale`

- Request: `multipart/form-data` — `file` 필드에 이미지 첨부
- Response: 업스케일된 이미지 파일 (현재는 원본과 동일)

## 실행

### Docker (권장)

```bash
# 빌드
docker build -t upscaling-api .

# 실행
docker run -p 4398:4398 upscaling-api
```

### 로컬

```bash
pip install -r requirements.txt
python main.py
```

서버는 `http://localhost:4398` 에서 실행됩니다.
