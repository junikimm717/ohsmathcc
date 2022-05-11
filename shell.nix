{ pkgs ? import <nixpkgs> {}, ... }:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python39Full
    poetry
    docker-compose
    # you really should have at least docker installed system-wide.
    scc
  ];
  MATHCC_DEV="true";
  shellHook = ''
source `poetry env info --path`/bin/activate
source ./dev
  '';
}
