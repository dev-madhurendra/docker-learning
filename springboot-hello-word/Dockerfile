FROM maven:3.8.5-openjdk-17 AS maven_build

WORKDIR /app

COPY pom.xml .
COPY src ./src

RUN mvn clean package

FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

COPY --from=maven_build /app/target/*.jar app.jar

EXPOSE 9091
ENTRYPOINT ["java", "-jar", "app.jar"]
