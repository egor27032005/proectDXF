
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class CorsConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**") // Разрешить CORS для всех endpoints
                .allowedOrigins("*") // Разрешить запросы со всех доменов
                .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS") // Разрешить все HTTP методы
                .allowedHeaders("*"); // Разрешить все заголовки
    }
}