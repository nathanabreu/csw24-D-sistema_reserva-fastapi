output "instance_public_ip" {
  value = aws_instance.fastapi_server.public_ip
}
