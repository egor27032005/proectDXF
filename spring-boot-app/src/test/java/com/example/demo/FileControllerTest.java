package com.example.demo;

import com.example.demo.controller.FileController;
import com.example.demo.service.FileService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.ResponseEntity;
import org.springframework.mock.web.MockMultipartFile;
import org.springframework.web.multipart.MultipartFile;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.when;

class FileControllerTest {

    @Mock
    private FileService fileService;

    @InjectMocks
    private FileController fileController;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void testUploadExcel() throws Exception {
        byte[] mockFileContent = "mock content".getBytes();
        MultipartFile mockMultipartFile = new MockMultipartFile("file", "test.xlsx", "application/vnd.ms-excel", mockFileContent);

        when(fileService.processExcel(any(MultipartFile.class), anyString())).thenReturn(mockFileContent);

        ResponseEntity<ByteArrayResource> response = fileController.uploadExcel(mockMultipartFile, "option");

        assertEquals(200, response.getStatusCodeValue());
        assertEquals(mockFileContent, response.getBody().getByteArray());
    }
}