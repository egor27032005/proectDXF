package com.example.demo;


import com.example.demo.service.FileService;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.ss.usermodel.WorkbookFactory;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.mock.web.MockMultipartFile;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import java.io.ByteArrayInputStream;
import java.io.IOException;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.when;

class FileServiceTest {

    @Mock
    private RestTemplate restTemplate;

    @InjectMocks
    private FileService fileService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void testProcessExcel() throws Exception {
        byte[] mockFileContent = "mock content".getBytes();
        MultipartFile mockMultipartFile = new MockMultipartFile("file", "test.xlsx", "application/vnd.ms-excel", mockFileContent);

        Workbook mockWorkbook = WorkbookFactory.create(new ByteArrayInputStream(mockFileContent));
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.MULTIPART_FORM_DATA);

        when(restTemplate.postForObject(anyString(), any(HttpEntity.class), any())).thenReturn(mockFileContent);

        byte[] result = fileService.processExcel(mockMultipartFile, "option");

        assertArrayEquals(mockFileContent, result);
    }
}