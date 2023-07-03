package com.sportnews.api.dto;

import java.time.LocalDateTime;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Data;

@Data
@Document
public class GameDto {
	
	@Id
	private String id;
	private String title;
	private Summary summary;
	private Status status;
	private LocalDateTime date;
	
}
