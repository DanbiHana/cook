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
    public void run(String... args) {
        if ("create".equalsIgnoreCase(ddlAuto)) {
            try {
                System.out.println("DDL-AUTO 값이 'create'입니다. Python 스크립트를 실행합니다.");

                ProcessBuilder processBuilder = new ProcessBuilder("python",
                        "C:\\project\\cook\\src\\main\\resources\\templates\\sql\\first_insert.py");
                processBuilder.redirectErrorStream(true);
                Process process = processBuilder.start();

                int exitCode = process.waitFor();
                System.out.println("Python 스크립트 종료 코드: " + exitCode);

                if (exitCode == 0) {
                    System.out.println("Python 스크립트가 정상적으로 실행되었습니다.");
                } else {
                    System.err.println("Python 스크립트 실행 중 문제가 발생했습니다.");
                }

            } catch (Exception e) {
                System.err.println("Python 스크립트를 실행하는 동안 예외가 발생했습니다: " + e.getMessage());
                e.printStackTrace();
            }
        } else {
            System.out.println("DDL-AUTO 값이 'create'가 아니므로 Python 스크립트를 실행하지 않습니다.");
        }
    }
}
