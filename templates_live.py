metadata_template = {
    '': '''{{
        "deleted": false,
        "lastModified": "{0}000",
        "metadatamodified": false,
        "modified": false,
        "parent": "{1}",
        "pinned": false,
        "synced": false,
        "type": "CollectionType",
        "version": 0,
        "visibleName": "{2}"
    }}''',
    '.pdf': '''{{
        "deleted": false,
        "lastModified": "{0}000",
        "metadatamodified": false,
        "modified": false,
        "parent": "{1}",
        "pinned": false,
        "synced": false,
        "type": "DocumentType",
        "version": 1,
        "visibleName": "{2}"
    }}''',
    '.epub': '''{{
        "deleted": false,
        "lastModified": "{0}000",
        "metadatamodified": false,
        "modified": false,
        "parent": "{1}",
        "pinned": false,
        "synced": false,
        "type": "DocumentType",
        "version": 1,
        "visibleName": "{2}"
    }}'''
}

content_template = {
    '': '''{{
    }}''',
    '.pdf': '''{{
        "extraMetadata": {{
        }},
        "fileType": "pdf",
        "fontName": "",
        "lastOpenedPage": 0,
        "lineHeight": -1,
        "margins": 100,
        "pageCount": 1,
        "textScale": 1,
        "transform": {{
            "m11": 1,
            "m12": 1,
            "m13": 1,
            "m21": 1,
            "m22": 1,
            "m23": 1,
            "m31": 1,
            "m32": 1,
            "m33": 1
        }}
    }}''',
    '.epub': '''{{
        "extraMetadata": {{
        }},
        "fileType": "epub",
        "fontName": "",
        "lastOpenedPage": 0,
        "lineHeight": -1,
        "margins": 100,
        "pageCount": 1,
        "textScale": 1,
        "transform": {{
            "m11": 1,
            "m12": 1,
            "m13": 1,
            "m21": 1,
            "m22": 1,
            "m23": 1,
            "m31": 1,
            "m32": 1,
            "m33": 1
        }}
    }}'''
}

cmd_template = "gm convert -density 300 {0}[0]  -colorspace Gray -shave 5%x5% -resize 280x374 {1}.jpg"

#-separate -average