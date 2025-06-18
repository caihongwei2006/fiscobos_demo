#!/usr/bin/env python3
"""
FiscoBOS农产品溯源系统 - 安装验证脚本
用于验证项目是否正确安装和配置
"""

import sys
import os
import sqlite3
import subprocess
import importlib.util

def print_header():
    print("=" * 60)
    print("🔍 FiscoBOS农产品溯源系统 - 安装验证")
    print("=" * 60)

def check_python_version():
    """检查Python版本"""
    print("\n📋 检查Python版本...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python版本: {version.major}.{version.minor}.{version.micro} (满足要求)")
        return True
    else:
        print(f"❌ Python版本: {version.major}.{version.minor}.{version.micro} (需要3.8+)")
        return False

def check_virtual_environment():
    """检查是否在虚拟环境中"""
    print("\n🏠 检查虚拟环境...")
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ 正在使用虚拟环境")
        return True
    else:
        print("⚠️  未检测到虚拟环境 (建议使用虚拟环境)")
        return True  # 不强制要求

def check_required_packages():
    """检查必需的Python包"""
    print("\n📦 检查必需的Python包...")
    required_packages = [
        'flask',
        'web3', 
        'sqlite3',  # 内置模块
        'sqlalchemy',
        'requests'
    ]
    
    all_installed = True
    for package in required_packages:
        try:
            if package == 'sqlite3':
                import sqlite3
            else:
                importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} (未安装)")
            all_installed = False
    
    return all_installed

def check_project_structure():
    """检查项目文件结构"""
    print("\n📁 检查项目文件结构...")
    required_files = [
        'src/main.py',
        'src/database/schema.sql',
        'src/database/db_manager.py',
        'src/api/routes.py',
        'config/app_config.py',
        'scripts/init_database.py',
        'requirements.txt'
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} (文件不存在)")
            all_exist = False
    
    return all_exist

def check_database():
    """检查数据库是否正确初始化"""
    print("\n🗄️  检查数据库...")
    db_path = 'database/products.db'
    
    if not os.path.exists(db_path):
        print("❌ 数据库文件不存在，请运行: python3 scripts/init_database.py")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # 检查表是否存在
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [table[0] for table in cursor.fetchall()]
        
        required_tables = ['products', 'suppliers', 'transactions']
        missing_tables = [table for table in required_tables if table not in tables]
        
        if missing_tables:
            print(f"❌ 缺少数据表: {missing_tables}")
            conn.close()
            return False
        
        print("✅ 数据库文件存在")
        print(f"✅ 数据表完整: {required_tables}")
        
        # 检查表结构
        for table in required_tables:
            cursor.execute(f"PRAGMA table_info({table});")
            columns = cursor.fetchall()
            print(f"✅ {table}表 ({len(columns)}列)")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ 数据库检查失败: {e}")
        return False

def check_configuration():
    """检查配置文件"""
    print("\n⚙️  检查配置文件...")
    try:
        sys.path.append('config')
        import app_config
        
        # 检查关键配置项
        if hasattr(app_config, 'DATABASE_URI'):
            print("✅ DATABASE_URI 配置存在")
        else:
            print("❌ DATABASE_URI 配置缺失")
            return False
            
        if hasattr(app_config, 'SECRET_KEY'):
            print("✅ SECRET_KEY 配置存在")
        else:
            print("❌ SECRET_KEY 配置缺失")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ 配置文件检查失败: {e}")
        return False

def check_permissions():
    """检查文件权限"""
    print("\n🔐 检查文件权限...")
    
    # 检查关键文件是否可读
    key_files = [
        'src/main.py',
        'scripts/init_database.py'
    ]
    
    all_readable = True
    for file_path in key_files:
        if os.access(file_path, os.R_OK):
            print(f"✅ {file_path} (可读)")
        else:
            print(f"❌ {file_path} (不可读)")
            all_readable = False
    
    # 检查数据库目录是否可写
    db_dir = 'database'
    if os.path.exists(db_dir):
        if os.access(db_dir, os.W_OK):
            print(f"✅ {db_dir}/ (可写)")
        else:
            print(f"❌ {db_dir}/ (不可写)")
            all_readable = False
    
    return all_readable

def run_basic_import_test():
    """运行基础导入测试"""
    print("\n🧪 运行基础导入测试...")
    
    try:
        # 测试主要模块导入
        sys.path.append('src')
        
        # 测试数据库模块
        from database.db_manager import DatabaseManager
        print("✅ 数据库模块导入成功")
        
        # 测试API模块
        from api import routes
        print("✅ API模块导入成功")
        
        return True
        
    except Exception as e:
        print(f"❌ 模块导入失败: {e}")
        return False

def provide_next_steps(all_passed):
    """提供下一步操作建议"""
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 恭喜！所有检查都通过了！")
        print("\n📋 下一步操作:")
        print("1. 启动应用: python3 src/main.py")
        print("2. 打开浏览器访问: http://localhost:5000")
        print("3. 运行测试: python -m pytest tests/ -v")
        print("4. 开始开发或使用系统功能")
    else:
        print("⚠️  部分检查未通过，请根据上述提示解决问题")
        print("\n🔧 常见解决方案:")
        print("1. 安装缺失的包: pip install -r requirements.txt")
        print("2. 初始化数据库: python3 scripts/init_database.py")
        print("3. 检查文件权限: chmod +x scripts/init_database.py")
        print("4. 确保在项目根目录运行此脚本")
    print("=" * 60)

def main():
    """主函数"""
    print_header()
    
    # 运行所有检查
    checks = [
        ("Python版本", check_python_version()),
        ("虚拟环境", check_virtual_environment()),
        ("必需包", check_required_packages()),
        ("项目结构", check_project_structure()),
        ("数据库", check_database()),
        ("配置文件", check_configuration()),
        ("文件权限", check_permissions()),
        ("模块导入", run_basic_import_test())
    ]
    
    # 统计结果
    passed = sum(1 for _, result in checks if result)
    total = len(checks)
    
    print(f"\n📊 检查结果: {passed}/{total} 项通过")
    
    # 显示失败的检查
    failed_checks = [name for name, result in checks if not result]
    if failed_checks:
        print(f"❌ 失败的检查: {', '.join(failed_checks)}")
    
    all_passed = passed == total
    provide_next_steps(all_passed)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
