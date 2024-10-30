-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/',F.BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE F INNER JOIN (SELECT BOARD_ID
FROM USED_GOODS_BOARD
ORDER BY VIEWS DESC
LIMIT 1) U ON F.BOARD_ID = U.BOARD_ID
ORDER BY F.FILE_ID DESC