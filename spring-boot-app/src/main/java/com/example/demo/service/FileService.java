package com.example.demo.service;


import org.apache.poi.ss.usermodel.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.Objects;

@Service
public class FileService {

//    private final String pythonServiceUrl = "http://localhost:5000/process-excel";
//    @Value("${PYTHON_SERVICE_URL}")
    public final String pythonServiceUrl = "http://python-app:5000/process-excel";

    public byte[] processExcel(MultipartFile file, String option) {
        try {
            // Проверка на наличие файла
            if (file == null || file.isEmpty()) {
                throw new IllegalArgumentException("Файл не был загружен");
            }

            // Проверка на наличие параметра
            if (option == null || option.isEmpty()) {
                throw new IllegalArgumentException("Параметр 'option' не был указан");
            }

            // Проверка на корректность формата файла
            if (!Objects.requireNonNull(file.getOriginalFilename()).endsWith(".xlsx") && !file.getOriginalFilename().endsWith(".xls")) {
                throw new IllegalArgumentException("Неподдерживаемый формат файла. Поддерживаются только .xlsx и .xls");
            }

            // Чтение Excel файла
            Workbook workbook = WorkbookFactory.create(file.getInputStream());
            Sheet sheet = workbook.getSheetAt(0);
            StringBuilder data = new StringBuilder();

            for (Row row : sheet) {
                for (Cell cell : row) {
                    data.append(cell.toString()).append(",");
                }
                data.append("\n");
            }

            // Создаем MultiValueMap для отправки файла и параметра
            MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();
            body.add("file", new org.springframework.core.io.ByteArrayResource(file.getBytes()) {
                @Override
                public String getFilename() {
                    return file.getOriginalFilename();
                }
            });
            body.add("option", option);

            // Создаем заголовки
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.MULTIPART_FORM_DATA);

            // Создаем HttpEntity с телом и заголовками
            HttpEntity<MultiValueMap<String, Object>> requestEntity = new HttpEntity<>(body, headers);

            // Отправляем запрос в Python программу
            RestTemplate restTemplate = new RestTemplate();
            ResponseEntity<byte[]> response = restTemplate.postForEntity(pythonServiceUrl, requestEntity, byte[].class);

            // Проверка ответа от Python сервиса
            if (response.getStatusCode() != HttpStatus.OK) {
                throw new RuntimeException("Ошибка при обработке файла на стороне Python сервиса: " + response.getStatusCode());
            }

            return response.getBody();
        } catch (IOException e) {
            throw new RuntimeException("Ошибка при обработке файла", e);
        } catch (IllegalArgumentException e) {
            throw new RuntimeException("Ошибка ввода данных: " + e.getMessage(), e);
        } catch (Exception e) {
            throw new RuntimeException("Неизвестная ошибка: " + e.getMessage(), e);
        }
    }
}