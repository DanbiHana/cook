package com.mbc.cook.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;
import java.io.BufferedReader;
import java.io.InputStreamReader;

@Component
public class PythonScriptRunner implements CommandLineRunner {
    @Value("${spring.jpa.hibernate.ddl-auto}")
    private String ddlAuto;

    @Override
    public void run(String... args) throws Exception {
        if ("create".equalsIgnoreCase(ddlAuto)) {
            // Python 스크립트 실행 로직 (위 코드와 동일)
            ProcessBuilder processBuilder = new ProcessBuilder("python", "C:\\project\\cook\\src\\main\\resources\\templates\\sql\\first_insert.py");
            Process process = processBuilder.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            int exitCode = process.waitFor();
            System.out.println("Python 스크립트 종료 코드: " + exitCode);
            System.out.println("종료 코드 0: 문제 없음");
        }
    }
}
