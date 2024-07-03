include project.conf

pip:
	@if [ -d ${VENV_DIR} ]; then \
		source ${VENV_BIN}/activate; \
		pip install pip --upgrade; \
		pip install -r requirements.txt; \
	else \
		echo "VENV does not exist. python -m venv venv"; \
	fi

clean:
	@if [ -d ${TARGET_DIR} ]; then \
		rm -f ${TARGET_DIR}/*.html; \
	else \
		echo "${TARGET_DIR} is not a directory"; \
	fi

build:
	@if [ -d ${SOURCE_DIR} ]; then \
		mkdir -p ${TARGET_DIR}; \
		cp -R ${CSS_DIR} ${TARGET_DIR}; \
		python main.py --source_dir ${SOURCE_DIR} --target_dir ${TARGET_DIR}; \
	else \
		echo "${SOURCE_DIR} is not a directory"; \
	fi

all: pip clean build

push_html:
	@aws s3 cp --recursive ${TARGET_DIR}/ ${S3_HTML_BUCKET};

push_media:
	@aws s3 cp --recursive ${MEDIA_DIR}/ ${S3_MEDIA_BUCKET}

refresh_cloudfront_html:
	@aws cloudfront create-invalidation --distribution-id ${CLOUDF_HTML} --paths "/*";

refresh_cloudfront_media:
	@aws cloudfront create-invalidation --distribution-id ${CLOUDF_MEDIA} --paths "/*";

publish: push_html refresh_cloudfront_html push_media refresh_cloudfront_media